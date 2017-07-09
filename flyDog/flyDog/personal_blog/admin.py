from django.contrib import admin

from personal_blog.models import Page_struct, Blog, Read


class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'p_type']
    list_display = ('title', 'release_time')
    list_filter = ['release_time']
    search_fields = ['title']
    date_hierarchy = 'release_time'

admin.site.register(Blog, BlogAdmin)
