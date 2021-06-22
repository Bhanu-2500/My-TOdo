from django.db import models

# Create your models here.


class Todo_items(models.Model):
    todo_name = models.CharField(max_length=30)
