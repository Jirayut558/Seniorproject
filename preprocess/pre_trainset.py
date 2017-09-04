import feature_option
import json
import csv
import re
import codecs

#input pathfile
#output type,subtitle,title,body
def getnews(pathfile):
    file = open(pathfile, 'r')
    i = 0
    for line in file.readlines():
        try:
            if(i==0):
                data = json.loads(line)
                i+=1
                if "dailynews" in pathfile:
                    return data['title']+data['subtitle'],data['body']
                else:
                    return data['title'],data['body']
        except Exception as e:
            continue


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
    out_list = [word,lable,seqofprg,countofw,isnum]
    return out_list

'''
input : newsfile.txt , start new seq , stop news seq
output : predata_x.csv * 10000 row/file
        tmp_csv 
'''

def pre_trainset(pathfile,start,stop):
    tmp_output = '/Users/jirayutk./Project/projectfile/pretrainset/'
    output_file = "predata_.csv"

    header = ['word' , 'lable' , 'seqofprg' , 'count' , 'isnum']

    file = open(pathfile, 'r')

    i = 0
    j = start
    k = stop
    index = 0

    csvfile = codecs.open(tmp_output + 'tmp_' + str(i) + '.csv', 'a','utf-8')
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for line in file.readlines():
        if j%10 == 0:
            print (str(j))

        if (index+1) < j and (index+1) >k:
            break
        try:
            data = json.loads(line)
            if "dailynews" in pathfile:
                title,body = data['title'] + data['subtitle'], data['body']
                list_word = feature_option.wordcut(re.sub(r"\s+", "", body).replace(" ", ""))
                for word in list_word:
                    list_data = get_feature_perword(word,title,body)
                    writer.writerow({header[0]:list_data[0], header[1]:list_data[1], header[2]:list_data[2], header[3]:list_data[3], header[4]:list_data[4],})
            else:
                title,body = data['title'], data['body']
        except Exception as e:
            print (e)
            continue
if __name__ == '__main__':
    pre_trainset("/Users/jirayutk./Project/projectfile/newsfile/dailynews/news_agriculture.txt",1,20)
