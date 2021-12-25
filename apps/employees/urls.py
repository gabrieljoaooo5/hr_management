from django.urls import path
from .views import (
    EmployeeList,
    EmployeeEdit,
    EmployeeDelete,
    EmployeeCreate
)

urlpatterns = [
    path('', EmployeeList.as_view(), name='list_employees'),
    path('new/', EmployeeCreate.as_view(), name='create_employee'),
    path('edit/<int:pk>/', EmployeeEdit.as_view(), name='update_employee'),
    path('delete/<int:pk>/', EmployeeDelete.as_view(), name='delete_employee'),

]