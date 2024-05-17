from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("contact/", views.contact),
    path("create/", login_required(views.CreatePostView.as_view()))
]
