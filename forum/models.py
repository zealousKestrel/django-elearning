from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
import uuid
from tinymce.models import HTMLField 

def handle_upload_to(instance,filename):
    return "{}-{}".format(instance.id,filename)

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return f"{self.id} : {self.name}"

class Forum(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = HTMLField()
    status = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified = models.DateTimeField(datetime.now(),null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)


    def __str__(self):
        return f"{self.id} : {self.title}"

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE)
    content = models.TextField(max_length=500,null=True,blank=True)
    published = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified = models.DateTimeField(datetime.now(),null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    file = models.FileField(upload_to=handle_upload_to)


    def __str__(self):
        return f"{self.id} : {self.user}"