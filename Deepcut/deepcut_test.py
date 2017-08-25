#-*-coding: utf-8 -*-
import deepcut
from bs4 import BeautifulSoup
import urllib.request
import string

url_news = "https://www.dailynews.co.th/economic/59098"
path_file = "/Users/jk/Projects/SeniorProject/Deepcut/newsfile/"
def get_news(url_text):
    response = urllib.request.urlopen(url_text)
    html = response.read()
    soup = BeautifulSoup(html,"html.parser")
    texts = ''
    for list in soup.find_all("section",class_=('article-detail')):
        for result in list.find_all("div",class_=('entry textbox content-all')):
            texts = result.get_text()
    texts = str(texts).replace("googletag.cmd.push(function() { googletag.display('div-gpt-ad-8668011-5'); });","").translate(str.maketrans('', '', string.whitespace))
    texts = texts.strip()
    return texts
def deep_word(url,path):
    text = get_news(url)
    list_word = deepcut.tokenize(text)
    write_file(list_word,path)
def write_file(listword,path):
    file = open(path,'w')
    file.write('|'.join(listword))
    file.close()
def main():   
    for i in range(10):
        url = url_news+str(i)
        path = path_file+str(i)+".txt"
        deep_word(url,path)
if __name__ == "__main__":
    main()