from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the employee')

    def __str__(self):
        return self.name
