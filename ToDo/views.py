from django import forms
from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    tasks = Task.objects.all()
    print(tasks)
    form = Todo_input()
    if request.method == 'POST':
        form = Todo_input(request.POST)
        if form.is_valid:
            form.save()
    context = {'tasks':tasks,'form':form}
    return render (request,'home.html',context)

class Todo_input(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        
