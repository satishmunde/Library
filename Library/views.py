from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
import random
from django.db.models import Q
from database.models import *
from datetime import date,datetime
import requests
import sqlite3

def adminpage(request):
    if request.user.is_anonymous:
        return redirect('/')
    
    
   
    return render(request,'admin.html')

def issue(request):
    book = Book.objects.all()
    if request.method == "GET":
        ser = request.GET.get('sear')
        
        try:
            # conn = sqlite3.connect('db.sqlite3')
            # cr= conn.cursor()
           
            
            # q = f"select * from database_book where title like '% {ser} %' or authors like '% {ser} %'"
            # print(q)
            # book = cr.execute(q)
            # print(book)
            # book = [row for row in cr.fetchall()]
            # print(book)
            
            # conn.commit()
            book = Book.objects.filter(Q(title__icontains=ser)|Q(authors__icontains = ser))
            
            return render(request,'isse.html',{'books':book})
            
        except Exception as e:
            print("error")
            print(e)



    if request.user.is_anonymous:
        return redirect('/')
    
    if request.method == "POST":
        
        bookid = request.POST.get('bookid')
        memid = request.POST.get('memid')
        rdate=request.POST.get('rdate')
       
   
        try:
            conn = sqlite3.connect("db.sqlite3")
            cr = conn.cursor()
       

            q1=f"""
                    SELECT username
                    FROM auth_user
                    WHERE username ='{memid}'
                  """ 
            cr.execute(q1)
            
            mem = cr.fetchone()
            # print(mem)
            # print(q1)
            
            
            if len(mem)!= 0:
                cr.execute(f"""
                    SELECT bookID
                    FROM database_book
                    WHERE bookID ='{bookid}'
                  """  )
                bk = cr.fetchall()
                print("TEst2")
                print(bk)
             
                if len(bk) !=0:
                    # print("test pass")
                    cr.execute(f"""
                    SELECT outstanding_debt
                    FROM database_librarymember
                    WHERE memid ='{memid}'
                  """ )
                    
                    bal = cr.fetchone()
                    print(bal)
                    for a in bal:
                        # print("Done")
                        
                        if a>=20:   
                            print("TEst4")                 
                            # rdate = datetime.strptime(rdate,'%m/%d/%Y'),
                            data =[bookid,memid,date.today(),rdate]
                            print(rdate)
                            cr.execute(f"insert into database_LibraryTransaction (book,member,issue_date,return_date)  values(?,?,?,?)",data)
                            conn.commit()
                            
                            cr.execute(f"update database_book set quantity_in_stock = quantity_in_stock-{1}  where bookID = '{bookid}' ")

                            conn.commit()
                            print("Done")
                
                            
                    

        except Exception as e:
            print(e)
            conn.rollback()

        finally:
            conn.close()
            
    # try:
    #     conn = sqlite3.connect("db.sqlite3")
    #     cr = conn.cursor()
    #     cr.execute("select book,member,return_date from database_LibraryTransaction ")

            
    #     data = cr.fetchall()
    #     conn.commit()

    # except Exception as e:
    #     print(e)
    #     print("Error")

    # finally:
    #     conn.close()
            
            
    return render(request,'isse.html',{'books':book})

def bookrtrn(request):
    if request.user.is_anonymous:
        return redirect('/')
    try:
        conn = sqlite3.connect('db.sqlite3')
        cr = conn.cursor()
        cr.execute(f"select book,member, issue_date,return_date from database_librarytransaction")
        info = cr.fetchall()
  
    
        # print(request.user)

        conn.commit()
        # print(info)
        
        
    except Exception as e:
        print(e)
    finally:
        conn.close()
    # print(book)
    if request.method == "POST":
        fee=request.POST.get('fee')
        bookid = request.POST.get('bookid')
        memid = request.POST.get('memid')
        try:
            conn = sqlite3.connect("db.sqlite3")
            cr = conn.cursor()

            cr.execute(f"Delete from database_LibraryTransaction where book ='{bookid}' and member='{memid}' ")
            conn.commit()
            cr.execute(f"update database_book set quantity_in_stock = quantity_in_stock + 1  where bookID = '{bookid}'")
            conn.commit()
            cr.execute(f"update database_librarymember set outstanding_debt = outstanding_debt-{fee}  where memid = '{memid}' ")
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()

        finally:
            conn.close()
            
        

    return render(request,'brtrn.html ',{'info':info})
    

def memdtl(request):
    if request.user.is_anonymous:
        return redirect('/')
    bal = request.POST.get("rech")
    if request.user.is_anonymous:
        return redirect('/')
    try:
        conn = sqlite3.connect('db.sqlite3')
        cr = conn.cursor()
        cr.execute(f"select book, issue_date,return_date from database_librarytransaction where member = '{request.user}'")
        info = cr.fetchall()
        cr.execute(f"Select outstanding_debt from database_librarymember where memid  ='{request.user}'")
        a = cr.fetchone()
        if a != None:
            for b in a:
                c=b  

      


        conn.commit()
        # print(info)
        
        
    except Exception as e:
        print(e)
    finally:
        conn.close()
    
    if request.method == "POST":
            
        try:
            conn=sqlite3.connect('db.sqlite3')
            cr = conn.cursor()
            cr.execute(f"Select memid from database_librarymember where memid  ='{request.user}'")
            id = cr.fetchone()
           
            # print(type(bal))  
            # print(c)
            if id is None and int(bal)<500:
                # print('done') 
                # print(bal)
                # print(request.user)
                pass
                    
            
        
                # conn.commit
                # print("Query Execute")
            elif int(c)<500 and int(bal)<500 and int(c+int(bal))<501: 
                cr.execute(f"update database_librarymember set outstanding_debt = outstanding_debt+{bal}  where memid = '{request.user}' ")
                conn.commit()

        except Exception as e:
            print(e)
            print("error")
        finally:
            conn.close()
            print("done")
    return render(request,'memdtl.html',{'b':a,'info':info})
    
def home(request):

    
    if request.method == "POST":
        username = request.POST.get("email")
        pwd = request.POST.get("password")

        user = authenticate(username = username,password=pwd)
        
        if username == "Admin":
            
            login(request,user)
            return redirect("/admin")
        
        else:
            login(request,user)
            return redirect('/memdtl')
        

    return render(request,'index.html')
    

def logoutUser(request):


    logout(request)
    return redirect('/')

def member(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        phone = request.POST.get('lname')
        
        email=request.POST.get('email')
        pass1=request.POST['pass']
        pass2=request.POST['re-pass']

            # if len(phone) !=0:
            #     mem = LibraryMember(memid = phone,outstanding_debt=0)
            #     mem.save()

            #     mem.close()
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            pass1=make_password(request.POST['pass'])
            user = User(first_name=fname , username= phone,email=email,password=pass1)
            mem =LibraryMember(memid= phone,outstanding_debt= 0)
            mem.save()
                
             
              
            user.save()
             
                
            return redirect('/')

            
            


    return render (request,'member.html')
    


def books(request):
    responce = requests.get('https://frappe.io/api/method/frappe-library?page=2&title=and').json()
    try:
      
        conn = sqlite3.connect('db.sqlite3')
        cr = conn.cursor()
        cr.execute("select * from database_book")

        data = cr.fetchall()

        if len(data)==0:
            print("Test2")
            for i in responce.items():
                l = i[1:]

                for a in l:
            
        
                    for item in a:
    
                        
                        book = Book(


                                    bookID =item['bookID'] ,
                                    
                                    title=item['title'],
                                    authors=item['authors'],
                                    average_rating =item['average_rating'] ,
                                    isbn=item['isbn'],
                                    isbn13=item['isbn13'],
                                    language_code =item['language_code'] ,
                                    num_pages=item['  num_pages'].replace("  ", ""),
                                    ratings_count=item['ratings_count'],
                                    text_reviews_count =item['text_reviews_count'] ,
                                    publication_date=datetime.strptime(item['publication_date'],'%m/%d/%Y'),
                                    publisher=item['publisher'],
                                    
                                    
                                
                                    quantity_in_stock=200
                                    # Add more fields as needed
                                )
                        book.save()
    except Exception as e:
        print(e)
        print("errors")

    finally:
        
        conn.close()
    

    return render(request,'books.html',{'data':responce})

