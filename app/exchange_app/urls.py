from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('', auth),
    path('index/', index),
    path('debts/', debts, name="debts"),
    path('teachers/', teachers, name="teachers"),
    path('teachers/add_teacher', add_teacher, name="add_teacher"),
    path('users/', users, name="users"),
    path('users/edit/<int:user_id>', user_edit, name="user_edit"),
    path('admins/', admins, name='admins'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path('timetable/', timetables, name="timetables"),
    path('edit_requests/', edit_requests, name="edit_requests"),
    path('table_requests/', table_request, name="table_requests"),
    path('admins/<int:admin_id>', change_admin, name='change_admin'),
    path('admins/delete_admin/<int:admin_id>', delete_admin, name='delete_admin'),
    path('admins/create_admin/', create_admin, name='create_admin')
]

