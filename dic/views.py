from django.shortcuts import render
from django import forms
from dic.getdata import getdata
# Create your views here.

class Entry(forms.Form):#clase para permitir que el usuario entre la palabra
    entrada=forms.CharField(max_length=100, required=False, label='')

def hello(request):
    
    word=Entry(request.POST)    
    contexto={'entrada':'','form':word}

    if(request.method=="POST"):#mostrar resultados
        result=getdata(request.POST['entrada'])
        contexto={'entrada':result[0],'datos':result[1],'form':word}
        return render(request,'extends.html',contexto)
    #mostrar la pantalla inicial
    return render(request,'index.html',contexto)
    
