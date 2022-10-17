from django.contrib import admin

# Register your models here.
from .models import Book, Post,Comment

# admin.site.register(Post)
# customizing post model display 
admin.site.register(Book)   
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish','status')
    list_filter=('status', 'created', 'publish','author')
    search_fields=('title', 'body')
    prepopulated_fields={'slug': ('title',)}
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=('status', 'publish')
    
@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    list_display =('name','email','post','created','active')
    list_filter = ('active','created','updated')
    search_fields =('name','email','body')