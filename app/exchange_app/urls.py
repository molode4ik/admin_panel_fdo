from django.urls import path
from .views import auth, index, teachers


urlpatterns = [
    path('', auth),
    path('index/', index, name="ind"),
    path('teachers/', teachers, name="teachers")
    path('users/', users, name="users")
]

