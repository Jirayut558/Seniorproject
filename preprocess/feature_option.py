import deepcut
import json
import re


#input : article
#output : list of word
def wordcut(article):
    list_word = deepcut.tokenize(article)
    return list_word

#input : title(cut),word(cut)
#output : 1 pass, 0 fail
def lable_intitle(word,title):
    try:
        title.index(word)
        return True
    except:
        return False

#input : word , body
#output : sequence of paragraph 0 - 1 (seq/total seq)
def seq_paragraph(word,body):
    list_body = str(body).splitlines()
    list_paragraph = []

    for line in list_body:
        if " " in line:
            despace = re.sub(r"\s+", "", line).replace(" ", "")
            list_paragraph.append(wordcut(despace))

    #--- check word in paragraph ---#
    for i,text in enumerate(list_paragraph):
        try:
            text.index(word)
            seqnum = i+1
            break
        except:
            seqnum = 0
    return (seqnum/len(list_paragraph))

#input : word
#output : 1 = is num , 0 = not number
def number_check(word):
    if str(word).replace('.','').isdigit():
        return True
    else:
        return False

#input : word , body
#output : number of word in body
def word_counting(word,body):
    list_word = wordcut(re.sub(r"\s+", "", body).replace(" ", ""))
    wordseq = list_word.count(word)
    return wordseq


def getnews():
    pathfile = "/Users/jirayutk./Project/projectfile/newsfile/dailynews/news_education.txt"
    file = open(pathfile, 'r')
    i = 0
    for line in file.readlines():
        try:
            if(i==0):
                data = json.loads(line)
                i+=1
                return data['body']
        except Exception as e:
            continue


if __name__ == '__main__':
    #print (lable_intitle("สวัสดี",wordcut("วันนี้วันจันทร์สวัสดีนะครับ")))
    print (word_counting("นิว",getnews()))