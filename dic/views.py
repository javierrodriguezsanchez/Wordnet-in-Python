from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from nltk.corpus import wordnet
from dic.getdata import getdata
# Create your views here.

class Entry(forms.Form):
    entrada=forms.CharField(max_length=100, required=False, label='')
    def __str__(self):
        return '{}'.format(self.entrada)

def hello(request):
    word=Entry(request.POST)    
    contexto={'entrada':'','form':word}
    if(request.method=="POST"):
        result=getdata(request.POST['entrada'])
        contexto={'entrada':result[0],'datos':result[1],'form':word}
        return render(request,'extends.html',contexto)
    return render(request,'index.html',contexto)
    
