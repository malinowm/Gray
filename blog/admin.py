from blog.models import BlogPost, Tag
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post Info', {'fields':['title', 'tag']}),
        ('Date Info', {'fields':['pub_date', 'postno']}),
        ('Content', {'fields':['content']}),
        ('Comments', {'fields':['comments']}),
        ]
    list_display = ('title', 'pub_date', 'postno')
    list_filter = ['pub_date', 'tag']
    search_fields = ['title']
    date_heirarchy = 'pub_date'

class TagAdmin(admin.ModelAdmin):
    fields = ['tag']
    list_display = ['tag']


admin.site.register(BlogPost, BlogAdmin)
admin.site.register(Tag, TagAdmin)
