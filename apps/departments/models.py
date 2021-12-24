from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the department')

    def __str__(self):
        return self.name