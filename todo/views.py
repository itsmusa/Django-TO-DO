from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm

def todo_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    queryset = Task.objects.filter(done=False)
    query = Task.objects.filter(done=True)
    context = {
        'tasks': queryset,
        'form': form,
        'done': query,
    }

    return render(request, 'index.html', context)


def delete_all(request):
    tasks_done = Task.objects.filter(done=True)
    tasks_done.delete()
    return redirect('/')


def task_done(request, id):
    t = Task.objects.get(id=id)
    t.done = True
    t.save()
    return redirect('/')
