from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
            return redirect("index/")
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
def users(request):
    search_query = request.GET.get('search', '')

    user_data = [
        {
            "ID": "1",
            "FIO": "Сыс Артем Валерьевич",
            "Gradebook_number": "1242142",
            "Login": "Traxat"
        },
        {
            "ID": "2",
            "FIO": "Синяк Антон Валерьеич",
            "Gradebook_number": "442222",
            "Login": "SIMEN"
        },
        {
            "ID": "3",
            "FIO": "Зарыб Ос КАЧев",
            "Gradebook_number": "922645",
            "Login": "4el"
        },
        {
            "ID": "4",
            "FIO": "Сыс Сус СЫН",
            "Gradebook_number": "222222",
            "Login": "sys@"
        },
    ]

    find_data = []

    if search_query:
        for record in user_data:
            for val in record.values():
                if val.find(search_query) != -1:
                    find_data.append(record)
                    break
        user_data = find_data

    return render(request=request, template_name='exchange_app/users.html', context={'users': users, 'user_data': user_data})


@login_required()
def admins(request):
    ...






































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
