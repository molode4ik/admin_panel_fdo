from django.db import models
from django.views import View
from .forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class Post(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()


class Users(models.Model):
    FIO = models.CharField(max_length=150)
    Gradebook_number = models.IntegerField()
    Login = models.CharField(max_length=150)

    def __str__(self):
        return self.FIO


#

# class Login(View):
#     template_name = 'exchange_app/login.html'
#
#     def get(self, request):
#         context = {
#             'form': UserCreationForm()
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index')
#         context = {
#             'form': form
#         }
#         return render(request, self.template_name, context)
