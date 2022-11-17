from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from .scripts import check_auth, search_users, hash_password


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
    if request.method == 'POST':
        if search_query:
            find_data = search_users(search_query, user_data)
            user_data = find_data
    if request.user.has_perm('exchange_app.change_users'):
        # Здесь открывает страницу измениея пользователя
        ...
    return render(request=request, template_name='exchange_app/users.html', context={'user_data': user_data})


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
