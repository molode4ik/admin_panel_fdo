from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Teachers, SimpleTable
from django.contrib.auth import authenticate, login
from .scripts import check_auth
from django.contrib.auth.hashers import make_password


def auth(request):
    if request.method == 'GET':
        return render(request=request, template_name='exchange_app/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        if check_auth(username=username, password=password):
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("exchange_app:ind")
        else:
            return render(request=request, template_name='exchange_app/login.html')


@login_required()
def index(request):
    if request.method == 'GET':
        print('aye')
        return render(request=request, template_name='exchange_app/index.html')

    if request.method == 'POST':
        ...


@login_required()
def teachers(request):
    ...
    # get_teachers = Teachers.objects.all()
    # table_teachers = SimpleTable(get_teachers)
    # print(get_teachers)
    # if request.method == 'GET':
    #     return render(request, 'exchange_app/teachers.html', {'table_teachers': table_teachers})












































@login_required()
def admins(request):
    data = []
    req = {
        'admin_name': 'name',
        'admin_login': 'login',
        'admin_password': 'password',
        'admin_privilege': 'privilege'
    }
    if request.POST:
        ...
    return render(request=request, template_name='exchange_app/admins.html', context={'data': data})
