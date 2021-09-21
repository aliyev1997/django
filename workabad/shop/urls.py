from . import views
from django.urls import path
from .views import *

urlpatterns = [

    path('',WorkHome.as_view(),name='home'),

    path('show_post/<int:post_id>/',ShowPost.as_view(),name='show_post'),
    path('add_comment/<int:post_id>/',AddComment.as_view(), name='add_comment'),
    path('registration/',RegisterUser.as_view(),name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

    path('show_category/<int:category_id>/',ShowCategory.as_view(),name='show_category'),
    path('show_tag/<int:tag_id>/', ShowTag.as_view(), name='show_tag'),




]
