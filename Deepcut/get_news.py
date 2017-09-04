#-*-coding: utf-8 -*-
import urllib.request
import json
from bs4 import BeautifulSoup
import os

url_dailynews = "https://www.dailynews.co.th/economic?page="
url_kaosod = "https://www.khaosod.co.th/around-thailand/page/"
path_file = "/Users/jirayutk./Project/projectfile/newsfile/"

url_matichon = "https://www.matichon.co.th/category/politics/page/"

# ------------------------------------------------DailyNews-------------------------------------------
def get_dailynews_url(url_page):
    response = urllib.request.urlopen(url_page)
    html = response.read()

    soup = BeautifulSoup(html, "html.parser")
    for x in soup.find_all("div", class_=('left')):
        for xx in x.find_all("article",class_=('content ')):
            link = xx.a.get('href')
            print(link)
            get_news(link)
def get_news(url_text):
    body = ''
    title = ''
    subtitle = ''
    type = ''
    inNews = False

    response = urllib.request.urlopen(url_text)
    html = response.read()

    soup = BeautifulSoup(html,"html.parser")
    for list in soup.find_all("section",class_=('article-detail')):
        for result in list.find_all("div",class_=('entry textbox content-all')):
            body = result.get_text()
    body = body.replace("googletag.cmd.push(function() { googletag.display('div-gpt-ad-8668011-5'); });","")#.translate(str.maketrans('', '', string.whitespace))
    for tag in soup.find_all("ol",class_=('breadcrumb')):
        if "ข่าวเดลินิวส์" in str(tag.find_all("li")):
            isNews = True
            for tag2 in tag.find_all("li"):
                type = tag2.get_text()
                if "ข่าวเดลินิวส์" not in str(tag2) and "หน้าแรก" not in str(tag2):
                    type = tag2.get_text()
        else:
            isNews = False
            break

    type = type.strip()
    title = soup.find("h1",class_=('title')).get_text().strip()
    subtitle = soup.find("p", class_=('desc')).get_text().strip()
    tmp = soup.find("span", class_=('date')).get_text().strip()
    subtitle = str(subtitle).replace(tmp,"")
    if isNews:
        if("เศรษฐกิจ-นวัตกรรมขนส่ง" in type):
            add_json(type,title,subtitle,body)
        else:
            print(type)

def add_json(type,title,subtitle,body):
    data = {"type": str(type).strip(), "title": str(title).strip(), "subtitle": str(subtitle).strip(),
            "body": str(body).strip()}
    json_data = json.dumps(data)
    file = open(path_file+"dailynews/news_education.txt",'a')
    file.writelines(json_data+"\n")
    file.close()

def load_dailynews_tofile():
    for i in range(601,650):
        print(str(i))
        get_dailynews_url(url_dailynews+str(i))

#------------------------------------------------DailyNews-------------------------------------------

#------------------------------------------------Kaosod-------------------------------------------
def get_kaosod_url(url_text):
    response = urllib.request.urlopen(url_text)
    html = response.read()

    soup = BeautifulSoup(html, "html.parser")
    for x in soup.find_all("div",class_=('ud_loop_inner')):
        for link in x.find_all("h3",class_=('entry-title td-module-title')):
            urllink = link.a.get('href')
            print(urllink)
            get_kaosod_news(urllink)
def get_kaosod_news(url_link):
    type = ""
    title = ""
    body = ""

    response = urllib.request.urlopen(url_link)
    html = response.read()

    soup = BeautifulSoup(html, "html.parser")
    for x in soup.find_all("div",class_=('entry-crumbs')):
        for xx in x.find_all("a"):
            if "หน้าแรก" not in xx.get_text():
                type = xx.get_text()
    for x in soup.find_all("h1",class_=('entry-title')):
        title = x.get_text()
    for x in soup.find_all("p"):
        body = body+x.get_text()
    write_file_kaosod(type, title, body)
    '''if "การเมือง" in type:
        #print(type,title,body)
        #write_file_kaosod(type,title,body)
    else:
        print(type)'''
def write_file_kaosod(type,title,body):
    data = {"type": str(type).strip(), "title": str(title).strip(),"body": str(body).strip()}
    json_data = json.dumps(data)
    file = open(path_file + "matichon/news_politics.txt", 'a')
    file.writelines(json_data + "\n")
    file.close()
def load_kaosod():
    for i in range(261,464):
        print (str(i))
        get_kaosod_url(url_kaosod+str(i))
 #------------------------------------------------Kaosod-------------------------------------------

#------------------------------------------------matichon----------------------------------------
def get_urls_matichon(url_page):
    response = urllib.request.urlopen(url_page)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all("h3",class_=('entry-title td-module-title')):
        link = tag.a.get('href')
        print(link)
        get_kaosod_news(link)
def load_matichon():
    for i in range(12,100):
        print (str(i))
        get_urls_matichon(url_matichon+str(i))
#------------------------------------------------matichon----------------------------------------



#--------------------------------------------Read News file -----------------------------------
def read_news(path_file):
    file = open(path_file,'r')
    for line in file.readlines():
        data = json.loads(line)
        print(data)

def sum_news(folderpath):
    listfile = os.listdir(folderpath)
    for file in listfile:
        if "news" in file:
            print(file)
            num_lines = sum(1 for line in open(folderpath+"/"+file))
            print(num_lines)

def main():
    try:
        #load_kaosod()
        load_matichon()
        #load_dailynews_tofile()
        #sum_news("/Users/jirayutk./Project/projectfile/newsfile/matichon")
    except Exception as e:
        print(e)
if __name__ == '__main__':
    main()