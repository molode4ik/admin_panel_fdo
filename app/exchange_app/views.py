from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from .scripts import check_auth, search_users, search_admin, search_user
from .api_requests import get_admins, get_students


def auth(request):
    if request.user.is_authenticated:
        return redirect("index/")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if check_auth(username=username, password=password):
            user = authenticate(username=username, password=password)
            login(request, user)
            print(user.get_group_permissions())
            return redirect("index/")
    return render(request=request, template_name='exchange_app/login.html')


@login_required()
def logout(request):
    logout(request)
    return redirect('auth/')


@login_required()
def index(request):
    return render(request=request, template_name='exchange_app/index.html')


@permission_required("exchange_app.view_teachers")
@login_required()
def teachers(request):
    ...
    # get_teachers = Teachers.objects.all()
    # table_teachers = SimpleTable(get_teachers)
    # print(get_teachers)
    # if request.method == 'GET':
    return render(request, 'exchange_app/teachers.html')


@permission_required("exchange_app.view_users")
@login_required()
def users(request):
    search_query = request.POST.get('search', '')
    user_data = get_students()
    if request.method == 'POST':
        if search_query:
            find_data = search_users(search_query, user_data)
            user_data = find_data

    request.session['user_data'] = user_data
    return render(request=request, template_name='exchange_app/users.html', context={'user_data': user_data})


@permission_required("exchange_app.change_users")
@login_required()
def user_edit(request, user_id):
    user_list = request.session['user_data']
    user = search_user(user_list, user_id)
    user_FIO = user['FIO'].split()
    return render(request=request, template_name='exchange_app/user_edit.html', context={'user': user, 'user_FIO': user_FIO})


@permission_required('auth.view_permission')
@login_required()
def admins(request):
    admins_data = get_admins()
    print(admins_data)
    request.session['admins_data'] = admins_data
    return render(request=request, template_name='exchange_app/admins.html', context={'admins_data': admins_data})


@permission_required('auth.change_permission')
@login_required()
def change_admin(request, admin_id):
    admins_list = request.session['admins_data']
    admin = search_admin(admins_list, admin_id)
    if request.method == "POST":
        send_data = {
            'admin_name': request.POST.get('admin_name'),
            'admin_privilege': request.POST.get('admin_privilege')
        }
        print(send_data)
        return redirect('http://127.0.0.1:8000/admins/')
    return render(request=request, template_name='exchange_app/admin.html', context=admin)


@permission_required('auth.delete_permission')
@login_required()
def delete_admin(request, admin_id):
    print('delete ', admin_id)
    return redirect('http://127.0.0.1:8000/admins/')
