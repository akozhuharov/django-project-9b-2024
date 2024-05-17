from django.shortcuts import render, redirect
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

    def post(self, request):
        form = PostForm(request.POST)
        if not form.is_valid():
            return render(request, "create.html", {"form": form, "error": True})
        post = Post(**form.cleaned_data)
        post.save()
        return redirect("/")

    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, "create.html", {"form": form})
