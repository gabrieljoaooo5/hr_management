from django.db import models
from django.contrib.auth.models import User
from apps.departments.models import Department
from apps.companies.models import Company


class Employee(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the employee')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departments = models.ManyToManyField(Department)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
