from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post
from .forms import PostForm
# Create your  views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


def contact(request):
    return HttpResponse("Contact page")


class CreatePostView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, "create.html", {"form": form})
