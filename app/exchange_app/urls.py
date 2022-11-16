from django.urls import path
from .views import auth, index, teachers, admins


urlpatterns = [
    path('', auth),
    path('index/', index),
    path('teachers/', teachers, name="teachers"),
    path('admins/', admins)
]

