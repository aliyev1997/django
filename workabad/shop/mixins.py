from .models import *


class DataMixin:
    def get_context_data(self, **kwargs):
        context=kwargs
        posts=Post.objects.all()
        context['posts']=posts
        return context
