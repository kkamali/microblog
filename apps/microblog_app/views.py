from django.shortcuts import render, redirect, reverse
from . import models

# Create your views here.
def index(request):
    all_posts = models.Blog.objects.all()
    context = {
        'posts' : all_posts
    }
    return render(request, "microblog_app/index.html", context)

def submit(request):
    user_name = request.POST["name"]
    microblog = request.POST["blog"]
    user_query = models.User(user_name = user_name)
    user_query.save()
    blog_query = models.Blog(context = microblog, user = user_query)
    blog_query.save()
    return redirect(reverse(index))
