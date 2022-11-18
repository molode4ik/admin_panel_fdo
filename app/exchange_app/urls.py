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
    path('users/edit_<int:user_id>', user_edit, name="user_edit"),
    path('admins/', admins),
    path("logout/", LogoutView.as_view(), name='logout'),
    path('admins/<int:admin_id>', change_admin, name='user_data'),
    path('admins/delete_admin/<int:admin_id>', delete_admin)
]

