from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def auth(request):
    if request.method == 'GET':
        return render(request=request, template_name='exchange_app/login.html')

    if request.method == 'POST':
        users = User.objects.values_list('username', flat=True)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username not in users:
            user = User.objects.create_user(username=username,
                                            password=password)
            user.save()
        print(users)
        #return render(request=request, template_name='exchange_app/index.html')
        return redirect("exchange_app:ind")


def index(request):
    if request.method == 'GET':
        print('aye')
        return render(request=request, template_name='exchange_app/index.html')

    if request.method == 'POST':
        ...
