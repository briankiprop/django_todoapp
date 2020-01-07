from django.shortcuts import render
from django.urls import reverse
from .models import ToDo
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    objects = ToDo.objects.all()
    context={
        'objects' : objects
    }

    return render(request, 'index.html',context)

def add_view(request):
    try:
        requesttest=request.POST
        addhead=request.POST.get('addhead')
        addtodo = request.POST.get('addtodo')
        ToDo.objects.create(head=addhead, todo=addtodo)
    except :
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def delete_view(request,id):
    object=ToDo.objects.get(id=id)

    object.delete()
    return HttpResponseRedirect('/')