from nltk.corpus import wordnet

def gettype(a):
    if a == 'n': return 'noun'
    if a == 'v': return 'verb'
    if a == 'r': return 'adverb'
    return 'adjetive'

def getdata(input):
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