from django.contrib import admin
from database.models import *

class Traction(admin.ModelAdmin):
    Dev_list = ('book','member','issue_date','return_date')

admin.site.register(LibraryTransaction,Traction)



class Mem(admin.ModelAdmin):
    Dev_list = ('memid','ourstanding_debt')

admin.site.register(LibraryMember,Mem)




class Books(admin.ModelAdmin):
    list=["bookID","title","authors","average_rating","isbn","isbn13","language_code","num_pages","ratings_count","text_reviews_count","publication_date","publisher","quantity_in_stock"]
    
    
admin.site.register(Book,Books)
    
