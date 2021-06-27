from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from django.views.generic import *
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Comment, Forum, Lesson
from .forms import ForumForm

import os

class forumDetailView(DetailView):
    model = Forum
    context_object_name = 'forum'

    def get_context_data(self, **kwargs):
        comment = Comment.objects.filter(forum=self.kwargs.get('pk'))
        self.kwargs.update({'comments':comment})
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

    def post(self,*args,**kwargs):
        message = self.request.POST.get('text')

        if self.request.user.is_authenticated:
            comment = Comment(user=self.request.user,forum=Forum.objects.get(id=kwargs.get('pk')),content=message)
            comment.save()
        return redirect(self.request.path_info+'#post-form')

class forumListView(ListView):
    model = Forum
    context_object_name = 'forum'

    def get_context_data(self, **kwargs):

        self.kwargs.update({'lesson':Lesson.objects.get(name=self.kwargs['lesson'])})
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

    def get_queryset(self,**kwargs):
        return super().get_queryset()

class lessonListView(ListView):
    model = Lesson
    
def index(request):
    return render(request,'index.html',{})
