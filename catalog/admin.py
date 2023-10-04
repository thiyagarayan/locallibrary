from django.contrib import admin
from .models import  Genre,language , Book, Author,BookInstance

#Register your models here.
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(language)
admin.site.register(Author)
admin.site.register(BookInstance)