from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.views.generic import (
                                DetailView,
                                TemplateView,
                                CreateView,
                                ListView,
                                )  

# Create your views here.

class AllPostsView(ListView):
    pass


class PostDetailView(DetailView):
    pass


class CreatePostView()