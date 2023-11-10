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
    aux=input.replace(' ','_')
    #nltk.download('wordnet')
    info=[
        {
            'name':a.name(),
            'type':gettype(a.pos()),
            'meaning':a.definition(),
            'Syn':list(filter(lambda x:x!=input, map(lambda x:x.name(),a.lemmas()))),
            'AnySyn':any(filter(lambda x:x.name()!=input,a.lemmas())),
            'Ant':list(map(lambda x:x.name(),a.lemmas()[0].antonyms())),
            'AnyAnt':any(a.lemmas()[0].antonyms()),
            'Hyper':list(map(lambda x:x.lemmas()[0].name(),a.hypernyms())),
            'AnyHyper':any(a.hypernyms()),
            'Hypo':list(map(lambda x:x.lemmas()[0].name(),a.hyponyms())),
            'AnyHypo':any(a.hyponyms()),
            'PHol':list(map(lambda x:x.lemmas()[0].name(),a.part_holonyms())),
            'AnyPHol':any(a.part_holonyms()),
            'PMer':list(map(lambda x:x.lemmas()[0].name(),a.part_meronyms())),
            'AnyPMer':any(a.part_meronyms()),
            'MHol':list(map(lambda x:x.lemmas()[0].name(),a.member_holonyms())),
            'AnyMHol':any(a.member_holonyms()),
            'MMer':list(map(lambda x:x.lemmas()[0].name(),a.member_meronyms())),
            'AnyMMer':any(a.member_meronyms()),
            'SMer':list(map(lambda x:x.lemmas()[0].name(),a.substance_meronyms())),
            'AnySMer':any(a.substance_meronyms()),
            'Ent':list(map(lambda x:x.lemmas()[0].name(),a.entailments())),
            'AnyEnt':any(a.entailments()),
            'Causes':list(map(lambda x:x.lemmas()[0].name(),a.causes())),
            'AnyCauses':any(a.causes()),
        }
        for a in wordnet.synsets(aux)
    ]

    return [input,info]