import feature_option
import json
import csv
import re
import codecs
import operator
import functools


#input : word,title,body
#output : list[]
'''
word , lable , seqofprg , count , isnum
'''
def get_feature_perword(word,title,body):
    lable = feature_option.lable_intitle(word,title)
    seqofprg = feature_option.seq_paragraph(word,body)
    countofw = feature_option.word_counting(word,body)
    isnum = feature_option.number_check(word)
    isdate = feature_option.date_check(word)
    pos = feature_option.pos_word(word)
    out_list = [word,lable,pos,seqofprg,countofw,int(isnum),int(isdate)]

    return out_list

'''
input : newsfile.txt , start new seq , stop news seq
output : predata_x.csv * 10000 row/file
        tmp_csv 
'''
def pre_trainset(pathfile,start,stop):
    tmp_output = ''
    output_file = "data/predata_.csv"

    header = ['word' , 'lable' , 'pos' , 'seqofprg' , 'count', 'isnum' ,'isdate']

    file = open(pathfile, 'r')

    i = 1
    j = start
    k = stop
    index = 0

    csvfile = codecs.open(tmp_output + 'predata_' + str(i) + '.csv', 'w','utf-8')
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for line in file.readlines():
        if (index+1)%10 == 0:
            if (index+1)%1000 == 0:
                i+=1
            print ("------ "+str(index+1)+"/"+k+"------")

        if (index+1) < j or (index+1) >k:
            index+=1
            break

        try:
            data = json.loads(line)
            if "dailynews" in pathfile:
                title,body = data['title'] + data['subtitle'], data['body']
            else:
                title,body = data['title'], data['body']
            list_title, list_body = feature_option.article_cut(title, body)
            list_word = functools.reduce(operator.concat, list_body)
            add_word = []
            for word in list_word:
                try:
                    add_word.index(word)
                except:
                    list_data = get_feature_perword(word, list_title, list_body)
                    add_word.append(word)
                    writer.writerow({header[0]: list_data[0], header[1]: int(list_data[1]), header[2]: list_data[2],
                                     header[3]: list_data[3], header[4]: list_data[4],
                                     header[5]: int(list_data[5]), header[6]: int(list_data[6])})
            index+=1
        except Exception as e:
            print (e)
            continue
if __name__ == '__main__':
    pre_trainset("/Users/jirayutk/Project/Seniorproject/newsfile/dailynews/news_economics.txt",1,2000)
