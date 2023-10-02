from django.contrib import admin
from .models import  Genre,language,book#author

# Register your models here.
admin.site.register(Genre)
admin.site.register(book)
admin.site.register(language)
#admin.site.register(author)