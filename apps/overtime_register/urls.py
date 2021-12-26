from django.urls import path
from .views import (
    OvertimeList,
    OvertimeEdit,
    OvertimeDelete,
    OvertimeCreate
)

urlpatterns = [
    path('', OvertimeList.as_view(), name='list_overtime'),
    path('new/', OvertimeCreate.as_view(), name='create_overtime'),
    path('edit/<int:pk>/', OvertimeEdit.as_view(), name='update_overtime'),
    path('delete/<int:pk>/', OvertimeDelete.as_view(), name='delete_overtime'),
]
