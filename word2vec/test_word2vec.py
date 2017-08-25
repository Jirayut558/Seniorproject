# -*- coding: utf-8 -*-
import os
from gensim import corpora, models, similarities
import logging
from collections import defaultdict
from pprint import pprint
import deepcut

def word_to_vec():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    documents = ['ฉันรักภาษาไทยเพราะฉันเป็นคนไทยและฉันเป็นคนไทย' ,'ฉันเป็นนักเรียนที่ชื่นชอบวิทยาศาสตร์และเทคโนโลยี' ,'ฉันไม่ใช่โปรแกรมเมอร์เพราะฉันทำมากกว่าคิดเขียนพัฒนาโปรแกรมทดสอบโปรแกรม','ฉันชื่นชอบวิทยาศาสตร์ชอบค้นคว้าตั้งสมมุติฐานและหาคำตอบ']
    texts = [list(deepcut.tokenize(i)) for i in documents]
    frequency = defaultdict(int)
    for text in texts:
            for token in text:
                frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 1] for text in texts]
    dictionary = corpora.Dictionary(texts)
    dictionary.save('/Users/jirayutk./Project/SeniorProject/word2vec/tmp/deerwester.dict') # store the dictionary, for future reference
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('/Users/jirayutk./Project/SeniorProject/word2vec/tmp/deerwester.mm', corpus) # store to disk, for later use
    print(texts)
    pprint(corpus)
def main():
    word_to_vec()

if __name__ == '__main__':
    main()