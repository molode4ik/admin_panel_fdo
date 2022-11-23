import json, csv
import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from .scripts import *
from .api_requests import *
from django.contrib import messages


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
        # пройтись циклом по файлу
    return render(request=request, template_name='exchange_app/teachers.html',
                  context={'teachers_data': teachers_data, 'flag': teachers_data})


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
    return render(request=request, template_name='exchange_app/teachers.html',
                  context={'modal_add': True, 'teachers_data': request.session['teachers']})


@permission_required("exchange_app.change_teachers")
@login_required()
def change_teacher(request, teacher_id):
    teachers_list = request.session['teachers']
    teacher = search_teacher(teachers_list, teacher_id)
    if request.method == "POST":
        send_data = {
            'teacher_id': teacher.get('teacher_id'),
            'name': request.POST.get('teacher_name'),
            'phone': request.POST.get('teacher_phone'),
            'email': request.POST.get('teacher_email'),
        }
        update_teacher(send_data)
        return redirect('/teachers')
    return render(request=request, template_name='exchange_app/teachers.html',
                  context={'teacher': teacher, 'modal': True, 'teachers_data': teachers_list})


@permission_required("exchange_app.delete_teachers")
@login_required()
def del_teacher(request, teacher_id):
    if request.method == 'POST':
        flag = delete_teacher(teacher_id)
        if flag != -1:
            messages.info(request, 'Удаление учителя прошло успешно')
        else:
            messages.info(request, 'Удалить учителя не удалось')
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
    group_list = get_groups()
    if request.method == 'POST':
        send_data = {
            'student_id': user_id,
            'group': request.POST.get('group'),
            'firstname': request.POST.get('firstname'),
            'lastname': request.POST.get('lastname'),
            'middlename': request.POST.get('middlename'),
            'email': request.POST.get('email'),
            'record_number': request.POST.get('recordnumber'),
            'eos_password': request.POST.get('email'),
            'eos_login': request.POST.get('recordnumber'),
        }
        return redirect('/users')
    return render(request=request, template_name='exchange_app/users.html',
                  context={'user': user, 'modal': True, 'user_data': user_list, 'groups': group_list})


@permission_required('auth.view_permission')
@login_required()
def admins(request):
    admins_data = get_admins()
    request.session['admins_data'] = admins_data
    return render(request=request, template_name='exchange_app/admins.html',
                  context={'admins_data': admins_data, 'flag': admins_data})


@permission_required('auth.change_permission')
@login_required()
def change_admin(request, admin_id):
    request.session['admins_type'] = ['admin', 'moderator', 'viewer']
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
    return render(request=request, template_name='exchange_app/admins.html',
                  context={'admin': admin, 'modal': True, 'admins_data': admins_list,
                           'admins_types': request.session['admins_type']})


@permission_required('auth.delete_permission')
@login_required()
def delete_admin(request, admin_id):
    if request.method == 'POST':
        flag = delete_admin_id(admin_id)
        if flag != -1:
            messages.info(request, 'Удаление Админа прошло успешно')
        else:
            messages.info(request, 'Удалить Админа не удалось')
        return redirect('/admins')


@permission_required('auth.delete_permission')
@login_required()
def create_admin(request):
    admins_list = request.session['admins_data']
    if request.method == "POST":
        send_data = {
            'name': request.POST.get('admin_name'),
            'login': request.POST.get('admin_login'),
            'password': hash_password(request.POST.get('admin_password')),
            'privilege': request.POST.get('admin_privilege'),
        }
        add_admin(send_data)
        return redirect('/admins')
    return render(request=request, template_name='exchange_app/admins.html',
                  context={'modal_add': True, 'admins_data': admins_list,
                           'admins_types': request.session['admins_type']})


@permission_required('exchange_app.view_post')
@login_required()
def timetables(request):
    ids = get_groups()
    shedule = get_shedule(ids[0])
    search_query = ids[0]
    if request.method == 'POST':
        search_query = request.POST.get('search')
        shedule = get_shedule(search_query)
    return render(request=request, template_name='exchange_app/timetable.html',
                  context={'number': ids, 'shedule': shedule, 'search_query': search_query})


@permission_required('exchange_app.view_post')
@login_required()
def update_timetable(request):
    flag = update_shedule()
    if flag != -1:
        messages.info(request, 'Обновление расписания прошло успешно')
    else:
        messages.info(request, 'Обновить расписание не удалось')
    return redirect('/timetable', contetx={'flag': flag})


@permission_required('exchange_app.view_post')
@login_required()
def table_requests(request):
    query_list = ['Подтверждение', 'Фидбек']
    if request.session.get('search_query') is None:
        request.session['search_query'] = query_list[0]
    if request.method == 'POST':
        search_query = request.POST.get('search')
        request.session['search_query'] = search_query
    data = get_data_from_req(request.session['search_query'])
    return render(request=request, template_name='exchange_app/table_request.html',
                  context={'search_value': request.session.get('search_query'), 'data': data, 'query_list': query_list})


@permission_required('exchange_app.change_post')
@login_required()
def remove_error_request(request, error_id: int):
    flag = del_error_request(error_id)
    if flag != -1:
        messages.info(request, 'Удаление запроса прошло успешно')
    else:
        messages.info(request, 'Удалить запрос не удалось')
    return redirect('/table_requests/', context={'flag': flag, 'search_query': request.session['search_query']})


@permission_required('exchange_app.change_post')
@login_required()
def confirm_request(request, confirm_id):
    flag = confirm_req(confirm_id)
    if flag != -1:
        messages.info(request, 'Подтверждение прошло успешно')
    else:
        messages.info(request, 'Подтверждение не удалось')
    return redirect('/table_requests/', context={'flag': flag, 'search_query': request.session['search_query']})


@permission_required('exchange_app.change_post')
@login_required()
def delete_confirm_request(request, confirm_id):
    flag = delete_confirm_req(confirm_id)
    if flag != -1:
        messages.info(request, 'Удаление прошло успешно')
    else:
        messages.info(request, 'Удаление не удалось')
    return redirect('/table_requests/', context={'flag': flag, 'search_query': request.session['search_query']})


@permission_required('exchange_app.change_post')
@login_required()
def edit_requests(request):
    return render(request=request, template_name='exchange_app/edit_requests.html')


@permission_required('exchange_app.change_post')
@login_required()
def debts(request):
    all_debts = get_all_academic_debts()
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES["document"]
        print(uploaded_file)
    request.session['debts'] = all_debts
    return render(request=request, template_name='exchange_app/debts.html', context={"debts": all_debts})


@permission_required('exchange_app.change_post')
@login_required()
def debts_see_more(request, academic_id):
    debts_list = request.session['debts']
    debt = search_debt(debts_list, academic_id)
    students = get_students()
    student = search_user(students, debt["academic_student_id"])
    return render(request=request, template_name='exchange_app/debts_see_more.html',
                  context={"debt": debt, "user": student})


@permission_required('exchange_app.change_post')
@login_required()
def delete_money_debt(request, money_id):
    flag = del_money_debt(money_id)
    if flag != -1:
        messages.info(request, 'Удаление задолжности прошло успешно')
    else:
        messages.info(request, 'Удалить задолжность не удалось')
    return redirect('/debts')


@permission_required('exchange_app.delete_post')
@login_required()
def delete_academic_debt(request, academic_id):
    flag = delete_debt(academic_id)
    if flag != -1:
        messages.info(request, 'Удаление задолжности прошло успешно')
    else:
        messages.info(request, 'Удалить задолжность не удалось')
    return redirect('/debts')
