from django.shortcuts import render,redirect,get_object_or_404
from . models import Task
from . forms import TaskForm

# Create your views here.

def home(request):
    tasks=Task.objects.all()
    return render(request,'todo/home.html',{'tasks':tasks})

def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request,'todo/add_task.html',{'form':form})

def update_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    if request.method=="POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request,'todo/update_task.html',{'form':form})

def delete_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect('home')

    