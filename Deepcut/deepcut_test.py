#-*-coding: utf-8 -*-
import deepcut
from bs4 import BeautifulSoup
import urllib.request
import string
from pythainlp.tag import pos_tag


path_file = "/Users/jk/Projects/SeniorProject/Deepcut/newsfile/"
def deep_word(text):
    #text = get_news(url)
    list_word = deepcut.tokenize(text)
    x = pos_tag(list_word, engine='artagger')
    print (x)
    #write_file(list_word,path)
def write_file(listword,path):
    file = open(path,'w')
    file.write('|'.join(listword))
    file.close()
def main():   
    deep_word("คณบดีกำลังนั่งคุยกับคุณครู ")
if __name__ == "__main__":
    main()