
from django.urls import path
from .views import *


urlpatterns = [
    path('',lessonListView.as_view(),name='lesson-list'),
    path('<str:lesson>',forumListView.as_view(),name='forum-list'),
    path('<str:lesson>/<str:pk>',forumDetailView.as_view(),name='forum-detail'),
]