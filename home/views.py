from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your  views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


def contact(request):
    return HttpResponse("Contact page")
