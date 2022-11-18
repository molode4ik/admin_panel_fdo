from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from .scripts import check_auth, search_users, hash_password, search_user, search_admin, parse_file
import json, csv
#from .config import Requests


def auth(request):
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
    teachers_data = [
        {
            "teacher_id": 1,
            "FIO": "Фоыр Фваы Соцфв",
            "Telephone_hunber": "88005553535"
        },
        {
            "teacher_id": 2,
            "FIO": "Кошфц Чвлцф БЬцвцф",
            "Telephone_hunber": "89996663344"
        },
        {
            "teacher_id": 3,
            "FIO": "Даыфв Сфыдв ГУаол",
            "Telephone_hunber": "85753150909"
        },
    ]

    if request.method == 'POST' and request.FILES:

        uploaded_file = request.FILES["document"]
        data = parse_file(uploaded_file)
        print(data)

        #пройтись циклом по файлу
    return render(request=request, template_name='exchange_app/teachers.html', context={'teachers_data': teachers_data})


def add_teacher(request):
    return render(request=request, template_name='exchange_app/add_teacher.html', context={})


@permission_required("exchange_app.view_users")
@login_required()
def users(request):
    search_query = request.POST.get('search', '')
    user_data = [
        {
            "ID": 1,
            "FIO": "Сыс Артем Валерьевич",
            "Gradebook_number": "1242142",
            "Login": "Traxat"
        },
        {
            "ID": 2,
            "FIO": "Синяк Антон Валерьеич",
            "Gradebook_number": "442222",
            "Login": "SIMEN"
        },
        {
            "ID": 3,
            "FIO": "Зарыб Ос КАЧев",
            "Gradebook_number": "922645",
            "Login": "4el"
        },
        {
            "ID": 4,
            "FIO": "Сыс Сус СЫН",
            "Gradebook_number": "222222",
            "Login": "sys@"
        },
    ]
    if request.method == 'POST':
        if search_query:
            find_data = search_users(search_query, user_data)
            user_data = find_data
    if request.user.has_perm('exchange_app.change_users'):
        # Здесь открывает страницу измениея пользователя
        ...
    request.session['user_data'] = user_data
    return render(request=request, template_name='exchange_app/users.html', context={'user_data': user_data})


def user_edit(request, user_id):
    user_list = request.session['user_data']
    user = search_user(user_list, user_id)
    user_FIO = user['FIO'].split()
    return render(request=request, template_name='exchange_app/user_edit.html', context={'user': user, 'user_FIO': user_FIO})


#@permission_required('permissions.view_permission')
@login_required()
def admins(request):
    user_data = [
        {
            'admin_id': 1,
            'admin_name': 'name',
            'admin_login': 'login',
            'admin_password': 'password',
            'admin_privilege': 'privilege'
        },
        {
            'admin_id': 2,
            'admin_name': 'name',
            'admin_login': 'login',
            'admin_password': 'password',
            'admin_privilege': 'privilege'
        },
    ]
    request.session['user_data'] = user_data
    return render(request=request, template_name='exchange_app/admins.html', context={'user_data': user_data})


@login_required()
def change_admin(request, admin_id):
    admins_list = request.session['user_data']
    admin = search_admin(admins_list, admin_id)
    if request.method == "POST":
        send_data = {
            'admin_name': request.POST.get('admin_name'),
            'admin_privilege': request.POST.get('admin_privilege')
        }
        print(send_data)
        return redirect('http://127.0.0.1:8000/admins/')
    return render(request=request, template_name='exchange_app/admin.html', context=admin)


@login_required()
def delete_admin(request, admin_id):
    print('delete ', admin_id)
    return redirect('http://127.0.0.1:8000/admins/')


def debts(request):
    if request.method == 'POST' and request.FILES:

        uploaded_file = request.FILES["document"]
        print(uploaded_file)
    return render(request=request, template_name='exchange_app/debts.html', context={})
