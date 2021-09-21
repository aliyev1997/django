from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_tag',kwargs={'tag_id':self.pk})




class Category(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('show_category', kwargs={'category_id': self.pk})


class Post(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    text=models.TextField()
    category = models.ForeignKey(Category, related_name='posts',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('link', kwargs={'post_id': self.pk})

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    text=models.TextField()






class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('User should have an email')
        if not username:
            raise ValueError('User should have an username')
        user=self.model(
            email=self.normalize_email(email),
            username=username,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class Account(AbstractBaseUser):
    email       =models.EmailField(max_length=60,verbose_name='email',unique=True)
    username    =models.CharField(max_length=30,unique=True)
    date_joined =models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login  =models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin    =models.BooleanField(default=False)
    is_active   =models.BooleanField(default=True)
    is_staff    =models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects=MyAccountManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ['username',]

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

