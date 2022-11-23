from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('', auth),
    path('index/', index),
    path('debts/', debts, name="debts"),
    path('debts/<int:debt_id>', debts_see_more, name="debts_see_more"),
    path('debts/create_debt', add_debt, name="add_debt"),
    path('teachers/', teachers, name="teachers"),
    path('teachers/add_teacher/', add_teacher, name="add_teacher"),
    path('teachers/<int:teacher_id>', change_teacher, name="change_teacher"),
    path('teachers/delete_teacher/<int:teacher_id>', del_teacher, name="del_teacher"),
    path('users/', users, name="users"),
    path('users/<int:user_id>', user_edit, name="user_edit"),
    path('admins/', admins, name='admins'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path('timetable/', timetables, name="timetables"),
    path('update_timetable/', update_timetable, name="update_timetable"),
    path('table_requests/', table_requests, name='table_requests'),
    path('table_requests/delete_error/<int:error_id>', remove_error_request, name='remove_error_request'),
    path('table_requests/confirm_request/<int:confirm_id>', confirm_request, name='confirm_request'),
    path('table_requests/delete_confirm_request/<int:confirm_id>', delete_confirm_request, name='delete_confirm_request'),
    path('admins/<int:admin_id>', change_admin, name='change_admin'),
    path('admins/delete_admin/<int:admin_id>', delete_admin, name='delete_admin'),
    path('admins/create_admin/', create_admin, name='create_admin'),
]

