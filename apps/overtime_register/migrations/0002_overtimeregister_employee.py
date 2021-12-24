# Generated by Django 4.0 on 2021-12-24 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_company_employee_departments_employee_user'),
        ('overtime_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='overtimeregister',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='employees.employee'),
            preserve_default=False,
        ),
    ]
