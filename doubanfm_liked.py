#coding=utf-8
from BeautifulSoup import BeautifulSoup
from urllib import urlencode
import urllib,urllib2,cookielib,re,json,time
import login

#config
url_liked='http://douban.fm/mine?start=%d&type=liked'
project_path='D:\Programming\pythonproject\doubanfm_download\\'

def get(url):
    print url
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(str(content))
    for div in soup.findAll('div', {'class' : 'info_wrapper'}):
        p = div.find('div', {'class' : 'song_info'}).findAll("p")
        sid = div.find('div', {'class' : 'action'})['sid']
        try:
            print p,sid 
        except:
            print "song..."

def main():
    douban_login.login()
    try:
        start_page=int(raw_input('start page:'))
        end_page=int(raw_input('end page:'))
    except:
        print "input error"
    for i in range(end_page-start_page+1):
        get(url_liked%((i+start_page-1)*15))

if __name__=='__main__':
    main()
