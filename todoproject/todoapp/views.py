import re
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Todo
from .forms import TodoForm
from django.urls import reverse

def index(request):
    todos = Todo.objects.all()
    output = ", ".join([todo.title for todo in todos])
    context = {
        "todos": todos
    }

    return render(request, "todoapp/index.html", context)


class Detail(View):
    form_class = TodoForm
    template_name = "todoapp/detail.html"

    def get(self, request, todo_id):
        todo = get_object_or_404(Todo, pk=todo_id)
        form = self.form_class(instance=todo)
        return render(request, self.template_name, {"todo": todo, "form": form})

    
    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, pk=todo_id)
        form = self.form_class(request.POST, instance=todo)

        form.save()

        return redirect(reverse('todoapp:index'))