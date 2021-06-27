from django.urls import path, include
from .views import *
from django.conf import settings
from filebrowser.sites import site
from django.conf.urls.static import static


urlpatterns = [
    path('',assignmentListView.as_view(),name='assignment-list'),
    # path('<str:lesson>/<str:pk>',assignmentListView.as_view(),name='assignment-detail'),
    path('<str:lesson>/<str:pk>',AnswerCreateView.as_view(),name='answer-detail'),
    path('create/',assignmentCreateView.as_view(),name='assigment-create'),
    path('',upload_image,name='upload_image'),
]


