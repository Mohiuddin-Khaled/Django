from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from task.forms import TaskForm
from task.models import TaskModel


def createTask(request):
    task_data = TaskForm()
    if request.method == "POST":
        task_data = TaskForm(request.POST)
        if task_data.is_valid():
            task_data.save(commit=True)
            return redirect("homePage")

    return render(request, "task/task_data.html", {"task_data": task_data})


def editTask(request, t_id):
    # task = TaskModel.objects.get(id=t_id)
    task = TaskModel.objects.filter(id=t_id).first()
    task_data = TaskForm(instance=task)
    if request.method == "POST":
        task_data = TaskForm(request.POST, instance=task)
        if task_data.is_valid():
            task_data.save(commit=True)
            return redirect("homePage")

    return render(request, "task/task_data.html", {"task_data": task_data})


def deleteTask(request, t_id):
    try:
        task = TaskModel.objects.get(id=t_id)
        task.delete()
        return redirect("homePage")
    except TaskModel.DoesNotExist:
        return HttpResponseNotFound("task not found!")
