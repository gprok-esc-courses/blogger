from django.shortcuts import render, redirect

from blog.forms import BlogpostForm
from blog.models import Blogpost
from django.contrib.auth.models import User


def index(request):
    blogposts = Blogpost.objects.all()
    context = {'blogposts': blogposts}
    return render(request, 'blog/index.html', context)


def blogpost(request, slug):
    blogpost = Blogpost.objects.filter(slug=slug).first()
    context = {'blogpost': blogpost}
    return render(request, 'blog/blogpost.html', context)


def blog(request, username):
    bloguser = User.objects.filter(username=username).first()
    blogposts = Blogpost.objects.filter(user_id=bloguser.id)
    context = {
        'bloguser': bloguser,
        'blogposts': blogposts,
    }
    return render(request, 'blog/blog.html', context)


def user(request):
    user = request.user
    blogposts = Blogpost.objects.filter(user_id=user.id)
    context = {
        'blogposts': blogposts,
    }
    return render(request, 'blog/user.html', context)


def add_post(request):
    if request.method == 'POST':
        form = BlogpostForm(request.POST)
        if form.is_valid():
            blogpost = Blogpost()
            blogpost.title = form.cleaned_data['title']
            blogpost.slug = form.cleaned_data['slug']
            blogpost.content = form.cleaned_data['content']
            blogpost.user = request.user
            blogpost.save()
            return redirect('/user')
    else:
        form = BlogpostForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/addpost.html', context)