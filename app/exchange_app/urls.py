from django.urls import path
from .views import auth, index, teachers, users, admins


urlpatterns = [
    path('', auth),
    path('index/', index),
    path('teachers/', teachers, name="teachers"),
    path('users/', users, name="users"),
    path('admins/', admins),
]

