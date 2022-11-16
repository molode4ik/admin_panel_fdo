from django.db import models
import django_tables2 as tables
from django_tables2 import TemplateColumn
from django.views import View
from .forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class Teachers(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=200)
    teacher_email = models.CharField(max_length=200)
    teacher_phone = models.CharField(max_length=200)

    class Meta:
        db_table = 'teachers'


class SimpleTable(tables.Table):
    class Meta:
        model = Teachers
        template_name = "django_tables2/bootstrap.html"

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
