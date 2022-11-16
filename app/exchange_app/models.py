from django.db import models
import django_tables2 as tables
from django_tables2 import TemplateColumn
from django.views import View
from .forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()

