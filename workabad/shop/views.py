from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request,'shop/index.html',{'posts':posts})

def add_post(request):

    if request.method=='POST':
        form=AddPostForm(request.POST)
        form.save()
    else:
        form=AddPostForm()
    return render(request,'shop/add_post.html',{'form':form})

def show_post(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    form = AddCommentForm()

    if request.method=='POST':
        form=AddCommentForm(request.POST)
        form.save()
    else:
        form=AddCommentForm()
    return render(request,'shop/show_post.html',{'post':post,'form':form})

def add_comment(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method=='POST':
        form=AddCommentForm(request.POST)
        form.save()
    else:
        form=AddCommentForm()
    return render(request, 'shop/add_comment.html', {'post': post, 'form': form})

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


