#-*-coding: utf-8 -*-
import deepcut
from bs4 import BeautifulSoup
import urllib.request
import string

path_file = "/Users/jk/Projects/SeniorProject/Deepcut/newsfile/"
def deep_word(text):
    #text = get_news(url)
    list_word = deepcut.tokenize("สวัสดีครับอรชรทำอะไรอยู่หรอครับ")
    print (list_word)
    #write_file(list_word,path)
def write_file(listword,path):
    file = open(path,'w')
    file.write('|'.join(listword))
    file.close()
def main():   
    deep_word("สวัสดีครับอรชรทำอะไรอยู่หรอครับ")
if __name__ == "__main__":
    main()