from django.urls import path
from .views import auth, index


urlpatterns = [
    path('', auth),
    path('index/', index, name="ind"),
]

