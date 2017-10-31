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
    NLBL = 0
    NCMN = 0

    lable = feature_option.lable_intitle(word,title)
    seqofprg = feature_option.seq_paragraph(word,body)
    countofw = feature_option.word_counting(word,body)
    isnum = feature_option.number_check(word)
    isdate = feature_option.date_check(word)
    pos = feature_option.pos_word(word)
    vectors = feature_option.word_to_vec(word)
    try:
        if 'NLBL' in pos:
            NLBL = 1
        elif 'NCMN' in pos:
            NCMN = 1
    except:
        pos = 0

    out_list = [word, int(lable), pos,NCMN,NLBL, seqofprg, countofw, int(isnum), int(isdate)]

    #Extract list of vector to out_list
    for vector in vectors:
        out_list.append(vector)


    return out_list

'''
input : newsfile.txt , start new seq , stop news seq
output : predata_x.csv * 10000 row/file
        tmp_csv 
'''
def pre_trainset(pathfile,start,stop):
    tmp_output = 'data2/'

    header = ['word' , 'lable' , 'pos' ,'NCNM','NLBL', 'seqofprg' , 'count', 'isnum' ,'isdate']
    for i in range(1, 11):
        header.append("wv" + str(i))

    file = open(pathfile, 'r')

    i = 1
    j = start
    k = stop
    index = 0
    csvfile = codecs.open(tmp_output + 'predata_' + str(i) + '.csv', 'w', 'utf-8')
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerow(header)
    for line in file.readlines():

        if (index+1) >= j and (index+1) <=k:
            if (index + 1) % 10 == 0:
                if (index + 1) % 1000 == 0:
                    i += 1
                print("------ " + str(index + 1) + "/" + str(k) + "------")

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
                        writer.writerow(list_data)
                index+=1
            except Exception as e:
                print (e)
        else:
            index+=1

if __name__ == '__main__':
    pre_trainset("/Users/jirayutk/Project/Seniorproject/newsfile/dailynews/news_economics.txt",1,1000)
