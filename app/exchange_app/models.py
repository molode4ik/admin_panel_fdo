from django.db import models
import django_tables2 as tables
from django_tables2 import TemplateColumn

class teachers(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=200)
    teacher_email = models.CharField(max_length=200)
    teacher_phone = models.CharField(max_length=200)


    class Meta:
        db_table = 'teachers'


class simpleTable(tables.Table):
    class Meta:
        model = teachers
        template_name = "django_tables2/bootstrap.html"

