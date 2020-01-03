from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views.generic import (
    View, CreateView,TemplateView,
    ListView, DeleteView
)
# Create your views here.

def HelloWorld(request):
    return render("Hello World!")

class IndexView(TemplateView):
    template_name = 'index.html'

class ExpenseListView(ListView):
    context_object_name = 'expenses'
    model = models.Expenses

class CreateExpenseView(CreateView):
    fields = ('date','category','description','amount')
    model = models.Expenses

class DeleteExpenseView(DeleteView):
    model = models.Expenses
    success_url = reverse_lazy('expense:list')
