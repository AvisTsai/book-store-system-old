from django.contrib import admin

from .models import Author, Publish, classification, Tag, Book
# Register your models here.

admin.site.register(Author)
admin.site.register(Publish)
admin.site.register(classification)
admin.site.register(Tag)
admin.site.register(Book)