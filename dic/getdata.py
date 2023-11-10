from nltk.corpus import wordnet

#archivo principal logico
#si se desea cambiar para trabajar con Prolog es aqui el trabajo
#la funcion gettype debe retornar una lista con la palabra de entrada 
#y otra lista de diccionarios, uno por cada sentido de la palabra
#los diccionarios deben tener:
#nombre del sentido, tipo, significado, lista de sinonimos,antonimos,meronimos, holonimos,etc
# y un booleano por cada lista para decir si son vacias o no.
#si se cambian los nombres de las llaves ir a cambiarlos tambien en templates/extends.html



def gettype(a):#es importante que se de asi el tipo de palabra
    if a == 'n': return 'noun'
    if a == 'v': return 'verb'
    if a == 'r': return 'adverb'
    return 'adjetive'#hay dos tipos de adjetivos diferentes, pero son adjetivos al fin y al cabo

def getdata(input):
    aux=input.replace(' ','_')#para poder entrar palabras compuestas
    info=[
        {
            #ni me molestare en explicar esto, esto cumple con el molde del comentario de arriba
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