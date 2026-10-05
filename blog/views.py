from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    pk_url_kwarg = 'pk'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_create.html'

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_update.html'

class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('post_list')