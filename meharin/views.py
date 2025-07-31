from django.shortcuts import render, redirect, get_object_or_404
from .models import MeharinModel

def index(request):
    data = MeharinModel.objects.all()
    return render(request, 'meharin/index.html', {'data': data})

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        MeharinModel.objects.create(name=name, email=email, age=age)
        return redirect('index')
    return render(request, 'meharin/form.html')

def edit(request, id):
    person = get_object_or_404(MeharinModel, pk=id)
    if request.method == 'POST':
        person.name = request.POST['name']
        person.email = request.POST['email']
        person.age = request.POST['age']
        person.save()
        return redirect('index')
    return render(request, 'meharin/form.html', {'person': person})

def delete(request, id):
    person = get_object_or_404(MeharinModel, pk=id)
    person.delete()
    return redirect('index')
