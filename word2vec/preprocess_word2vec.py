# -*- coding: utf-8 -*-
#python process_wiki.py thwiki-latest-pages-articles.xml.bz2 wiki.th.text
import json
import string
import logging
import os.path
import sys
import re
import codecs
import deepcut
from gensim.corpora import WikiCorpus

tmp_path = "/Users/jirayutk/Project/Seniorproject/word2vec/tmp.text"
news_path= "/Users/jirayutk/Project/Seniorproject/word2vec/news_economics.txt"
output_path = "/Users/jirayutk/Project/Seniorproject/word2vec/economic.th.text"

def read_news_fromfile(path_file):
    global tmp_path
    input_file = open(path_file,'r')
    output_file = open(tmp_path,'w')
    text = ''
    count = 0
    for line in input_file.readlines():
        try:
            data = json.loads(line)
            count += 1
            body = data['body']
            text = text + re.sub(r"\s+", "", body).replace(" ", "") + "\n"
        except Exception as e:
            continue
    output_file.write(text)
    output_file.close()
    input_file.close()

def preprocess():
    global news_path,output_path,tmp_path
    read_news_fromfile(news_path)

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    inp = tmp_path
    outp = output_path
    space = ' '
    i = 0
    inputfile = open(inp,'r')
    output = open(outp, 'w')

    for line in inputfile.readlines():
        text = deepcut.tokenize(line)
        list1 = space.join(text)
        output.write((list1))
        i += 1
        if (i % 100 == 0) or (i <= 10 ):
            logger.info("Saved " + str(i) + " articles")
    output.close()
    logger.info("Finished Saved " + str(i) + " articles")

if __name__ == '__main__':
    preprocess()