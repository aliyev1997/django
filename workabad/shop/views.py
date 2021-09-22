from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import *
from .mixins import *
# Create your views here.

class WorkHome(DataMixin,ListView):
    model=Post
    template_name = 'shop/index.html'


    def get_context_data(self ,**kwargs):
        context=super().get_context_data(**kwargs)

        return context




class ShowCategory(ListView):
    model=Category
    template_name = 'shop/show_category.html'
    context_object_name = 'cat'

    def get_context_data(self):
        context=super().get_context_data()
        posts=Post.objects.filter(category_id=self.kwargs['category_id'])
        cat=Category.objects.get(id=self.kwargs['category_id'])
        context['posts']=posts
        context['cat']=cat
        return context

    #def get_queryset(self):
       # return Post.objects.filter(category_id=self.kwargs['category_id'])


class ShowTag(ListView):
    model=Tag
    template_name = 'shop/show_tag.html'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        posts=Post.objects.filter(tags__id=self.kwargs['tag_id'])
        context['posts']=posts
        return context
    def get_queryset(self):
        return Tag.objects.get(id=self.kwargs['tag_id'])


class ShowPost(ListView):
    model = Post
    template_name = 'shop/show_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        #post=Post.objects.get(id=self.kwargs['post_id'])
        #context['post']=post
        return context

    def get_queryset(self):
        return Post.objects.get(id=self.kwargs['post_id'])

class AddComment(CreateView):
    form_class=AddCommentForm
    template_name = 'shop/add_comment.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        post = Post.objects.get(id=self.kwargs['post_id'])
        context['post']=post
        return context


class RegisterUser(CreateView):
    form_class=Reqistration
    template_name = "shop/registration.html"

    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


