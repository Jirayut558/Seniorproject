import deepcut
import json
import re
import operator
import functools
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
    return (seqnum/len(list_body))

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
    return word_count

#if __name__ == '__main__':
    #word_counting("new",[[3,3],[4,5]])
