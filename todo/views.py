from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)



def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form, 'task': task}
    return render(request, 'update.html', context)


def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'delete.html', context)


def crossoff_item(request, pk):
    list_item = Task.objects.get(id=pk)
    list_item.status = True
    list_item.save()
    return redirect('/')

def uncross_item(request, pk):
    list_item = Task.objects.get(id=pk)
    list_item.status = False
    list_item.save()
    return redirect('/')
