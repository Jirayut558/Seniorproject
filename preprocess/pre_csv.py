import csv
import codecs

path_output = "/Users/jirayutk/Project/Seniorproject/preprocess/trainset.csv"
path_csv = "/Users/jirayutk/Project/Seniorproject/preprocess/data2/predata_1.csv"

csvfile = codecs.open('trainset.csv','a', 'utf-8')
writer = csv.writer(csvfile, lineterminator='\n')

#writer.writerow()
#'pos' ,'NCNM','NLBL', 'seqofprg' , 'count', 'isnum' ,'isdate'

count = 0
with codecs.open(path_csv,encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['lable'] == '1' and count < 5000:
            '''writer.writerow([row['NCNM'],row['NLBL'],row['seqofprg'],row['count'],row['isnum'],row['isdate'],
                             row['wv1'],row['wv10'],row['wv11'],row['wv12'],row['wv13'],row['wv14'],row['wv15'],row['wv16'],row['wv17'],row['wv18'],row['wv19'],row['wv100'],
                             row['wv2'],row['wv20'],row['wv21'],row['wv22'],row['wv23'],row['wv24'],row['wv25'],row['wv26'],row['wv27'],row['wv28'],row['wv29'],
                             row['wv3'],row['wv30'],row['wv31'],row['wv32'],row['wv33'],row['wv34'],row['wv35'],row['wv36'],row['wv37'],row['wv38'],row['wv39'],
                             row['wv4'],row['wv40'],row['wv41'],row['wv42'],row['wv43'],row['wv44'],row['wv45'],row['wv46'],row['wv47'],row['wv48'],row['wv49'],
                             row['wv5'],row['wv50'],row['wv51'],row['wv52'],row['wv53'],row['wv54'],row['wv55'],row['wv56'],row['wv57'],row['wv58'],row['wv59'],
                             row['wv6'],row['wv60'],row['wv61'],row['wv62'],row['wv63'],row['wv64'],row['wv65'],row['wv66'],row['wv67'],row['wv68'],row['wv69'],
                             row['wv7'],row['wv70'],row['wv71'],row['wv72'],row['wv73'],row['wv74'],row['wv75'],row['wv76'],row['wv77'],row['wv78'],row['wv79'],
                             row['wv8'],row['wv80'],row['wv81'],row['wv82'],row['wv83'],row['wv84'],row['wv85'],row['wv86'],row['wv87'],row['wv88'],row['wv89'],
                             row['wv9'],row['wv90'],row['wv91'],row['wv92'],row['wv93'],row['wv94'],row['wv95'],row['wv96'],row['wv97'],row['wv98'],row['wv99']
                             ,row['lable']])'''
            writer.writerow([row['NCNM'], row['NLBL'], row['seqofprg'], row['count'], row['isnum'], row['isdate'],
                             row['wv1'], row['wv2'],row['wv3'],row['wv4'],row['wv5'],row['wv6'],row['wv7'],row['wv8'],row['wv9'],row['wv10'],row['lable']])
            count+=1
    print(count)