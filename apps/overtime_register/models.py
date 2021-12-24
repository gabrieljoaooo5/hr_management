from django.db import models
from apps.employees.models import Employee


class OvertimeRegister(models.Model):
    reason = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.reason
