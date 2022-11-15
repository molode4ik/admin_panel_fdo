from django.urls import path
from .views import auth, index, teacher


urlpatterns = [
    path('', auth),
    path('index/', index, name="ind"),
    path('teacher/', teacher, name="teacher")
]

