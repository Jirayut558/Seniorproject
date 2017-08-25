# -*- coding: utf-8 -*-
#python process_wiki.py thwiki-latest-pages-articles.xml.bz2 wiki.th.text
import json
import string
import logging
import os.path
import sys
import re
import deepcut
from gensim.corpora import WikiCorpus

tmp_path = "/Users/jirayutk./Project/SeniorProject/word2vec/tmp.text"

def read_news_fromfile(path_file):
    input_file = open(path_file,'r')
    output_file = open(tmp_path,'w')
    text = ''
    count = 0
    for line in input_file.readlines():
        try:
            data = json.loads(line)
            count += 1
            body = data['body']
        except Exception as e:
            continue
        text = text + re.sub(r"\s+", "", body).replace(" ","") +"\n"
    output_file.write(text)
    output_file.close()
    input_file.close()

def preprocess(path_news):
    read_news_fromfile(path_news)

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 3:
        print((globals()['__doc__'] % locals()))
        sys.exit(1)
    inp, outp = sys.argv[1:3]
    space = ' '
    i = 0

    input = open(inp,'r')
    output = open(outp, 'w')

    for line in input.readlines():
        text = deepcut.tokenize(line)
        list1 = space.join(text)
        output.write((list1))
        i += 1
        if (i % 100 == 0):
            logger.info("Saved " + str(i) + " articles")
    output.close()
    logger.info("Finished Saved " + str(i) + " articles")
def main():
    path = "/Users/jirayutk./Project/SeniorProject/Deepcut/newsfile/dailynews/news_economics.txt"
    preprocess(path)

if __name__ == '__main__':
    main()