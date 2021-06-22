from django.shortcuts import render
from .models import Todo_items
from django.http import HttpResponseRedirect


def Home_view(request):
    obj = Todo_items.objects.all().order_by('-id')
    print(obj)
    return render(request, 'index.html', {'obj': obj})


def add_todo(request):
    q = Todo_items(todo_name=request.POST['content'])
    q.save()
    return HttpResponseRedirect('/')


def delete_todo(request, q):
    qdel = Todo_items.objects.get(id=q)
    qdel.delete()
    return HttpResponseRedirect('/')
