from django.http import HttpResponse
from django.template import RequestContext, Context, loader
from blog.models import BlogPost, Tag, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import calendar
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django import forms
from datetime import datetime

class CommentForm(forms.Form):
    name = forms.CharField(max_length=32)
    #email = forms.EmailField()
    content = forms.CharField()

    

def bloglist(request):
    
    blog_list = BlogPost.objects.all().order_by('-pub_date')
    paginator = Paginator(blog_list, 5)

    page = request.GET.get('page')
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
            # if page is not an integer, deliver the first page.
            blog_list  = paginator.page(1)
    except EmptyPage:
            #If page is out of range, deliever last page of results
            blog_list = pageinator.page(paginator.num_pages)
    
    t = loader.get_template('blog/list.html')
    c = Context({'blog_list':blog_list,})
    return HttpResponse(t.render(c))

@csrf_protect 
def singleblog(request, postNo):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = Comment(poster= form.cleaned_data['Name'], pub_date=datetime.now, content = form.cleaned_data['content'])
            blog = BlogPost.objects.filter(postno=postNo)[0]
            blog.update(comments=comment)

    b = BlogPost.objects.filter(postno=postNo)[0]

    

    t = loader.get_template('blog/blog.html')
    c = RequestContext(request, {'blog':b})
    return HttpResponse(t.render(c))

def about(request):

    t = loader.get_template('blog/about.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))
