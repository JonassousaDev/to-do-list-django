from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'task'

class TaskDetails(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task.html'