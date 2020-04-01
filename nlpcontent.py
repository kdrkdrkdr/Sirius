
from soynlp.postagger import *


pos_dict = {
    'Adverb': {'너무', '매우', }, 

    'Noun': {'노래', '날씨', '검색', '길'},
    
    'Josa' : {'을', '를', '좀'},

    'Verb': {'하는', '하다', '하고'},
    
    'Adjective': {'예쁜', '예쁘다'},
    
    'Exclamation': {'우와'},

    'Eomi': {}
}


dictionary = Dictionary(pos_dict)

generator = LRTemplateMatcher(dictionary)    

evaluator = LREvaluator()

postprocessor = UnknowLRPostprocessor()

tagger = SimpleTagger(generator, evaluator, postprocessor)




def NLPContent(Text):

    Text = Text.replace(' ', '')

    RevCharList = tagger.tag(Text)[::-1]

    for p in enumerate(RevCharList):
        idx = p[0]
        content = p[1][0]
        tag = p[1][1]

        if tag == 'Noun':
            index = idx 
            LastNoun = content   
            break

    for i in range(index, -1, -1):
        del RevCharList[i]

    RealCharList = RevCharList[::-1]

    RealContent = ""
    for c in RealCharList:
        RealContent += c[0]
    
    return (LastNoun, RealContent)

