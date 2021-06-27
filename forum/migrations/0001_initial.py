# Generated by Django 3.2.4 on 2021-06-07 10:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import forum.models
import tinymce.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('status', models.BooleanField(default=False)),
                ('published', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2021, 6, 7, 10, 50, 43, 372525))),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('content', models.TextField(blank=True, max_length=500, null=True)),
                ('published', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2021, 6, 7, 10, 50, 43, 373797))),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('file', models.FileField(upload_to=forum.models.handle_upload_to)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]