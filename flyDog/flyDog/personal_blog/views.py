from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from personal_blog.models import Blog, Read, Page_struct
from django.http import Http404
import json

def homepage(request):
    blogs = Blog.objects.all().order_by('-update_time')[:30]
    return render(request, 'personal_blog/homepage.html', {'blogs':blogs})

def blog_detail(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)[0]
    blogs = Blog.objects.filter(p_type=blog.p_type)
    return render(request, 'personal_blog/detail.html', {'blog':blog.body, 'blogs':blogs})

def blog_wiki(request, wiki_id):
    blogs = Blog.objects.filter(p_type=wiki_id)
    return render(request, 'personal_blog/wiki.html', {'blogs':blogs})

def blog_search(request):
    value = request.GET.get('Search', '')
    if value:
        blogs = Blog.objects.filter(body__icontains=value)
        return render(request, 'personal_blog/search.html', {'blogs':blogs})
    else:
        return HttpResponse('not input search value')