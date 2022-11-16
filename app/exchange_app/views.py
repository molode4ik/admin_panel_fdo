from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Teachers, SimpleTable
from django.contrib.auth import authenticate, login
from .scripts import check_auth, hash_password
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Post


def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = hash_password(request.POST.get('password'))
        flag, level = check_auth(username=username, password=password)
        if flag:
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect(f"index/")

    return render(request=request, template_name='exchange_app/login.html')


@login_required()
def index(request):
    request.user.user_permissions.add('some_shit')
    print(request.user.user_permissions)
    content_type = ContentType.objects.get_for_model(Post)
    post_permission = Permission.objects.filter(content_type=content_type)
    print([perm.codename for perm in post_permission])
    if request.method == 'POST':
        ...

    return render(request=request, template_name='exchange_app/index.html')


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


