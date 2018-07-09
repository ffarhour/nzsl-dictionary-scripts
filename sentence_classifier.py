import sys
import nltk

def get_nltk_classification(sentence):
    try:
        #sentence = str(sys.argv[1])
        sentence = sentence.lower()
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        sentence_tagged = []
        for word in tagged:
            if word[1] == 'CC':
                text ='coordinating conjunction'
            if word[1] == 'CD':
                text ='cardinal digit'
            if word[1] == 'DT':
                text ='determiner'
            if word[1] == 'EX':
                text ='existential there'
            if word[1] == 'FW':
                text ='foreign word'
            if word[1] == 'IN':
                text ='preposition/subordinating conjunction'
            if word[1] == 'JJ':
                text ='adjective'
            if word[1] == 'JJR':
                text ='adjective, comparative'
            if word[1] == 'JJS':
                text ='adjective, superlative'
            if word[1] == 'LS':
                text ='list marker'
            if word[1] == 'MD':
                text ='modal'
            if word[1] == 'NN':
                text ='noun, singular'
            if word[1] == 'NNS':
                text ='noun plural'
            if word[1] == 'NNP':
                text ='proper noun, singular'
            if word[1] == 'NNPS':
                text ='proper noun, plural'
            if word[1] == 'PDT':
                text ='predeterminer'
            if word[1] == 'POS':
                text ='possessive ending'
            if word[1] == 'PRP':
                text ='personal pronoun'
            if word[1] == 'PRP$':
                text ='possessive pronoun'
            if word[1] == 'RB':
                text ='adverb'
            if word[1] == 'RBR':
                text ='adverb, comparative'
            if word[1] == 'RBS':
                text ='adverb, superlative'
            if word[1] == 'RP':
                text ='particle'
            if word[1] == 'TO':
                text ='tokens'
            if word[1] == 'UH':
                text ='interjection'
            if word[1] == 'VB':
                text ='verb, base form'
            if word[1] == 'VBD':
                text ='verb, past tense'
            if word[1] == 'VBG':
                text ='verb, gerund/present participle'
            if word[1] == 'VBN':
                text ='verb, past participle'
            if word[1] == 'VBP':
                text ='verb, sing. present, non-3d'
            if word[1] == 'VBZ':
                text ='verb, 3rd person sing. present'
            if word[1] == 'WDT':
                text ='wh-determiner'
            if word[1] == 'WP':
                text ='wh-pronoun'
            if word[1] == 'WP$':
                text ='possessive wh-pronoun'
            if word[1] == 'WRB':
                text ='wh-abverb'
            sentence_tagged.append(text)
            #print("Word: ", word[0], "\t Classification:", text)
        return sentence_tagged
    except:
        pass
