from django.urls import reverse_lazy

from .models import OvertimeRegister
from .forms import OvertimeRegisterForm
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)


class OvertimeList(ListView):
    model = OvertimeRegister

    def get_queryset(self):
        company = self.request.user.employee.company
        return OvertimeRegister.objects.filter(employee__company=company)


class OvertimeEdit(UpdateView):
    model = OvertimeRegister
    form_class = OvertimeRegisterForm

    def get_form_kwargs(self):
        kwargs = super(OvertimeEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class OvertimeDelete(DeleteView):
    model = OvertimeRegister
    success_url = reverse_lazy('list_overtime')


class OvertimeCreate(CreateView):
    model = OvertimeRegister
    form_class = OvertimeRegisterForm

    def get_form_kwargs(self):
        kwargs = super(OvertimeCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
