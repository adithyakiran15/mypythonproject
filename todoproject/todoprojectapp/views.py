from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import Todoform
from django.views.generic import ListView
from  django.views.generic.detail import DetailView
from  django.views.generic.edit import UpdateView,DeleteView

class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'tasks'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detailview' , kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('homelistview')




# Create your views here.0.
def home(request):
    tasks = Task.objects.all()
    if request.method=="POST":

        name=request.POST.get('name','')
        priority=request.POST.get("priority",'')
        date=request.POST.get("date",'')
        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,'home.html',{'tasks':tasks})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')

    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=Todoform(request.POST or None, request.FILES, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f , 'task':task})