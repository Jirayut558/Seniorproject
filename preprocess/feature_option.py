# -*- coding: utf-8 -*-
import codecs
import deepcut
import json
import re
import operator
import functools
import csv
from pythainlp.tag import pos_tag
from pythainlp.tokenize import sent_tokenize
import gensim

model_path = "/Users/jirayutk/Project/Seniorproject/model/economic2.th.model"
model = gensim.models.Word2Vec.load(model_path)

'''
Word to Vector
input : word
output : vector of float [100 features]
'''
def word_to_vec(word):
    try:
        vec = (model.wv[word])
        return vec
    except:
        return [0]*10

'''
input : title , body
output : list(title) , list(body)
'''
def article_cut(title,body):
    list_body = str(body).splitlines()
    list_paragraph = []
    for line in list_body:
        if " " in line:
            despace = re.sub(r"\s+", "", line).replace(" ", "")
            list_paragraph.append(wordcut(despace))
    list_title = wordcut(re.sub(r"\s+", "", title).replace(" ", ""))
    return list_title,list_paragraph

#input : article
#output : list of word
def wordcut(article):
    list_word = deepcut.tokenize(article)
    return list_word
'''
phrase cut
input : article
output : list of phrase
'''
def phrasecut(article):
    list_in = sent_tokenize(article, engine='whitespace')
    list_out = []
    i=0
    while i < len(list_in):
        if list_in[i].isdigit():
            list_out.append(list_in[i]+list_in[i+1])
            i+=2
        else:
            list_out.append(list_in[i])
            i+=1
    return list_out


#input : title(cut),word(cut)
#output : 1 pass, 0 fail
def lable_intitle(word,list_title):
    try:
        list_title.index(word)
        return True
    except:
        return False

#input : word , body(list)
#output : sequence of paragraph 0 - 1 (seq/total seq)
def seq_paragraph(word,list_body):
    #--- check word in paragraph ---#
    for i,text in enumerate(list_body):
        try:
            text.index(word)
            seqnum = i+1
            break
        except:
            seqnum = 0
    n = len(list_body)
    return (n-seqnum+1/n)

#input : word
#output : 1 = is num , 0 = not number
def number_check(word):
    if str(word).replace('.','').isdigit():
        return True
    else:
        return False

#input : word , body
#output : number of word in body
def word_counting(word,list_body):
    list = functools.reduce(operator.concat, list_body)
    word_count = list.count(word)
    return word_count/len(list)

#input : word
#output : 1 = isDate 0 = notDate
def date_check(word):
    date =[]
    with open("checklist.csv", encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['day'] != '':
                date.append(row['day'])
            if row['month'] != '':
                date.append(row['month'])
    try:
        date.index(word)
        return True
    except:
        return False

#input : word
#output : POS
def pos_word(word):
    pos = pos_tag(word, engine='old')
    return pos[0][1]




if __name__ == '__main__':
    filein = codecs.open("input_article.txt","r",encoding='utf8')
    fileout = codecs.open("output_article.txt","w",encoding='utf8')
    input = filein.read()

    fileout.writelines("Word cut\n"+str(wordcut(input))+"\n\nPhrase cut\n"+str(phrasecut(input)))

