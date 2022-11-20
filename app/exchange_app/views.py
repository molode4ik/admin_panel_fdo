import json, csv
import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from .scripts import *
from .api_requests import *


def auth(request):
    if request.user.is_authenticated and request.session['user_password']:
        if check_auth(request.user.username, request.session['user_password']):
            return redirect("index/")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if check_auth(username=username, password=password):
            user = authenticate(username=username, password=password)
            login(request, user)
            request.session['user_password'] = password
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
    teachers_data = get_teachers()
    request.session['teachers'] = teachers_data
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES["document"]
        data = parse_file(uploaded_file)
        print(data)
        #пройтись циклом по файлу
    return render(request=request, template_name='exchange_app/teachers.html', context={'teachers_data': teachers_data})


@permission_required("exchange_app.delete_teachers")
@login_required()
def add_teacher(request):
    if request.method == 'POST':
        send_data = {
            'name': f"{request.POST.get('lastname')} {request.POST.get('firstname')} {request.POST.get('middlename')}",
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone')
        }
        create_teacher(send_data)
        return redirect('/teachers')
    return render(request=request, template_name='exchange_app/add_teacher.html', context={})


@permission_required("exchange_app.change_teachers")
@login_required()
def change_teacher(request, teacher_id):
    teachers_list = request.session['teachers']
    teacher = search_teacher(teachers_list, teacher_id)
    if request.method == "POST":
        send_data = {
            'teacher_id': teacher.get('teacher_id'),
            'name': request.POST.get('teacher_name'),
            'teacher_phone': request.POST.get('teacher_phone'),
            'teacher_email': request.POST.get('teacher_email'),
        }
        #update_admin(send_data)
        return redirect('/teachers')
    return render(request=request, template_name='exchange_app/teacher.html', context=teacher)


@permission_required("exchange_app.delete_teachers")
@login_required()
def del_teacher(request, teacher_id):
    #delete_admin_id(admin_id)
    return redirect('/teachers')


@permission_required("exchange_app.view_users")
@login_required()
def users(request):
    search_query = request.POST.get('search', '')
    user_data = get_students()
    if request.method == 'POST':
        if search_query:
            find_data = search_users(str(search_query), user_data)
            user_data = find_data

    request.session['user_data'] = user_data
    return render(request=request, template_name='exchange_app/users.html', context={'user_data': user_data})


@permission_required("exchange_app.change_users")
@login_required()
def user_edit(request, user_id):
    user_list = request.session['user_data']
    user = search_user(user_list, user_id)
    user_FIO = [user_list[0]["student_lastname"], user_list[0]["student_firstname"], user_list[0]["student_middlename"]]
    return render(request=request, template_name='exchange_app/user_edit.html', context={'user': user, 'user_FIO': user_FIO})


@permission_required('auth.view_permission')
@login_required()
def admins(request):
    admins_data = get_admins()
    request.session['admins_data'] = admins_data
    return render(request=request, template_name='exchange_app/admins.html', context={'admins_data': admins_data})


@permission_required('auth.change_permission')
@login_required()
def change_admin(request, admin_id):
    admins_list = request.session['admins_data']
    admin = search_admin(admins_list, admin_id)
    if request.method == "POST":
        send_data = {
            'admin_id': admin_id,
            'name': request.POST.get('admin_name'),
            'privilege': request.POST.get('admin_privilege')
        }
        update_admin(send_data)
        return redirect('/admins')
    return render(request=request, template_name='exchange_app/admin.html', context=admin)


@permission_required('auth.delete_permission')
@login_required()
def delete_admin(request, admin_id):
    delete_admin_id(admin_id)
    return redirect('/admins')


@permission_required('auth.delete_permission')
@login_required()
def create_admin(request):
    if request.method == "POST":
        send_data = {
            'name': request.POST.get('admin_name'),
            'login': request.POST.get('admin_login'),
            'password': hash_password(request.POST.get('admin_password')),
            'privilege': request.POST.get('admin_privilege'),
        }
        add_admin(send_data)
        return redirect('/admins')
    return render(request=request, template_name='exchange_app/create_admin.html')


@permission_required('exchange_app.view_post')
@login_required()
def timetables(request):
    ids = get_groups()
    if request.method == 'POST':
        search_query = request.POST.get('search')
        shedule = get_shedule(search_query)
        request.session["search"] = search_query
        return render(request=request, template_name='exchange_app/timetable.html', context={'shedule': shedule, 'number': ids})
    return render(request=request, template_name='exchange_app/timetable.html', context={'number': ids})


def table_request(request):
    table = [
        {
            "id": "88",
            "FIO": "Хорошун Данил Алексеевич",
            "numbers": "89876561278",
            "record_book": "432123",
            "view_requests": "Смена пароля"

        },
        {
            "id": "89",
            "FIO": "Соколов Денис Александрович",
            "numbers": "897686544319",
            "record_book": "980543",
            "view_requests": "подтверждение зачетки"
        },
        {
            "id": "90",
            "FIO": "Ряпалов Дмитрий Николаевич",
            "numbers": "89172191267",
            "record_book": "970676",
            "view_requests": "Chill"
        }
        ]

    if request.method == 'POST':
        data = request.POST['data']
        data_id = re.findall('(\d+)', data)
        data_users = [i for i in table if i['id'] == data_id[0]]

        return render(request=request, template_name='exchange_app/edit_requests.html', context={ 'data_users': data_users})
    return render(request=request, template_name='exchange_app/table_request.html', context={'table': table})


def edit_requests(request):

    return render(request=request, template_name='exchange_app/edit_requests.html')


@permission_required('exchange_app.change_post')
@login_required()
def debts(request):
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES["document"]
        print(uploaded_file)
    return render(request=request, template_name='exchange_app/debts.html', context={})
