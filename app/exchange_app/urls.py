from django.urls import path
from .views import auth, index, teachers, users, admins, logout, user_edit
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('', auth),
    path('index/', index),
    path('teachers/', teachers, name="teachers"),
    path('users/', users, name="users"),
    path('users/edit_<int:user_id>', user_edit, name="user_edit"),
    path('admins/', admins),
    path("logout/", LogoutView.as_view(), name='logout'),
]

