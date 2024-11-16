from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from todos.models import Todo

def home(request):
    return render(request, 'todos/home.html')

class TodoListView(ListView):
    model=Todo
    template_name= 'todos/todo_list.html'
    
class TodoUpdateView(UpdateView):
    model=Todo
    fields= ['tittle', 'deadline']
    template_name= 'todos/todo_form.html'
    success_url= reverse_lazy('todo_list')
    
class TodoCreateView(CreateView):
    model=Todo
    fields= ['tittle', 'deadline']
    template_name= 'todos/todo_form.html'
    success_url= reverse_lazy('todo_list')
    
class TodoDeleteView(DeleteView):
    model=Todo
    template_name= 'todos/todo_confirm_delete.html'
    success_url= reverse_lazy('todo_list')