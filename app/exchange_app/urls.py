from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('', auth),
    path('index/', index),
    path('debts/', debts, name="debts"),
    path('debts/see_more/<int:academic_id>', debts_see_more, name="debts_see_more"),
    path('teachers/', teachers, name="teachers"),
    path('teachers/add_teacher/', add_teacher, name="add_teacher"),
    path('teachers/<int:teacher_id>', change_teacher, name="change_teacher"),
    path('teachers/delete_teacher/<int:teacher_id>', del_teacher, name="del_teacher"),
    path('users/', users, name="users"),
    path('users/edit/<int:user_id>', user_edit, name="user_edit"),
    path('admins/', admins, name='admins'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path('timetable/', timetables, name="timetables"),
    path('update_timetable/', update_timetable, name="update_timetable"),
    path('edit_requests/', edit_requests, name="edit_requests"),
    path('errors/', table_request_errors, name='table_request_errors'),
    path('errors/delete_error/<int:error_id>', remove_error_request, name='remove_error_request'),
    path('confirms/', table_request_confirms, name='table_request_confirms'),
    path('confirms/confirm_request/<int:confirm_id>', confirm_request, name='confirm_request'),
    path('confirms/delete_confirm_request/<int:confirm_id>', delete_confirm_request, name='delete_confirm_request'),
    path('admins/<int:admin_id>', change_admin, name='change_admin'),
    path('admins/delete_admin/<int:admin_id>', delete_admin, name='delete_admin'),
    path('admins/create_admin/', create_admin, name='create_admin'),
    path('debts/delete_academic_debt/<int:academic_id>', delete_academic_debt, name='delete_academic_debt')
]

