
#python train_word2vec_model.py wiki.th.text wiki.th.text.model wiki.th.text.vector

# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import multiprocessing
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
 
if __name__ == '__main__':
    inp = "/Users/jirayutk./Project/projectfile/word2vec/education.th.text"
    outp1 = "/Users/jirayutk./Project/projectfile/word2vec/education.th.model"
    outp2 = "/Users/jirayutk./Project/projectfile/word2vec/education.th.vector"

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,
            workers=multiprocessing.cpu_count())
 
    # trim unneeded model memory = use(much) less RAM
    #model.init_sims(replace=True)
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)

