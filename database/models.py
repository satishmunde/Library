from django.db import models
from django.contrib.auth.models import User



class LibraryTransaction(models.Model):
    book = models.CharField(max_length=10)
    member = models.CharField(max_length=200)
    issue_date = models.DateField()
    return_date = models.DateField()
   




class LibraryMember(models.Model):
    # username = models.ForeignKey(User,on_delete=models.CASCADE)
    memid = models.CharField(max_length=10)
    outstanding_debt = models.DecimalField(max_digits=10, decimal_places=2)




class Book(models.Model):
    bookID = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    average_rating = models.CharField(max_length=4)
    isbn = models.CharField(max_length=13)
    isbn13 = models.CharField(max_length=13)
    language_code = models.CharField(max_length=10)
    num_pages = models.CharField(max_length=5)
    ratings_count = models.CharField(max_length=5)
    text_reviews_count = models.CharField(max_length=5)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=255)

    quantity_in_stock = models.IntegerField()
      
    
    

