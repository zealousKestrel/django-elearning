from django.contrib import admin


from .models import Forum, Comment, Lesson

admin.site.register(Lesson)
admin.site.register(Forum)
admin.site.register(Comment)