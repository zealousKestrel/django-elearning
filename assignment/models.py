from django.db import models
from django.contrib.auth.models import User
from forum.models import Lesson 

import uuid
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField

def handle_upload_to(instance,filename):
    return "{}-{}".format(instance.id,filename)

class Assignment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='Lesson',)
    title = models.CharField(max_length=255)
    published = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    content = RichTextUploadingField()
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id} : {self.user}"

class Answer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = RichTextUploadingField()
    file = models.FileField(upload_to=handle_upload_to,null=True,blank=True)
    published = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified = models.DateTimeField(datetime.now(),null=True,blank=True)
    

    def __str__(self):
        return f"{self.id} : {self.user}"