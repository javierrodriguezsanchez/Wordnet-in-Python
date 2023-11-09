from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from nltk.corpus import wordnet
# Create your views here.

class Entry(forms.Form):
    entrada=forms.CharField(max_length=100, required=False, label='')
    def __str__(self):
        return '{}'.format(self.entrada)

def hello(request):
    word=Entry(request.POST)    
    contexto={'entrada':'','form':word}
    if(request.method=="POST"):
        result=datas(request.POST['entrada'])
        contexto={'entrada':result[0],'datos':result[1],'form':word}
        return render(request,'extends.html',contexto)
    return render(request,'index.html',contexto)
    
def gettype(a):
    if a == 'n': return 'noun'
    if a == 'v': return 'verb'
    if a == 'r': return 'adverb'
    return 'adjetive'

def datas(input):

    #nltk.download('wordnet')
    info=[
        {
            'name':a.name(),
            'type':gettype(a.pos()),
            'meaning':a.definition(),
            'Syn':list(filter(lambda x:x!=input, map(lambda x:x.name(),a.lemmas()))),
            'Ant':list(map(lambda x:x.name(),a.lemmas()[0].antonyms())),
            'Hyper':list(map(lambda x:x.name(),a.hypernyms())),
            'Hypo':list(map(lambda x:x.name(),a.hyponyms()))
        }
        for a in wordnet.synsets(input)
    ]

    return [input,info]