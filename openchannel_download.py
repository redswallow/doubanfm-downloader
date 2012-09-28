# coding=utf-8
from urllib import urlencode
import urllib,urllib2,cookielib,json,time,os

#config
keyword="aniDa"
cate="album" #singer,album
limit="1"
url='http://douban.fm/j/open_channel/creation/search'
project_path='C:\doubanfm_download\\'
download_path='C:\music\\'
cookie='flag="ok"; ck="drmb"; dbcl2="2386246:qSC8IzUu8dU"; bid="XO73zFY2spw"'

def build_search_url(keyword,cate="misc",limit=""):
    data={'keyword':keyword,
          'cate':cate,
          'limit':limit
    }
    url_data=urlencode(data)
    return url_data

def get_songs(url,url_data,cookie):
    #build request
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(opener)
    req = urllib2.Request(url+'?'+url_data)
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
    req.add_header('Cookie', cookie)
    #get json
    content=urllib2.urlopen(req).read()
    dict=json.loads(content)
    #get songs
    songs=dict["data"]["songs"]
    return songs

def get_songs_info(songs):
    for song in songs:
        for key in song:
            print key,song[key]

def get_songs_info(songs,index):
    song=songs[index]
    for key in song:
        print key,song[key]

def download(songs):
    folder=create_folder()
    for song in songs:
        log(song['name']+song['artist']+song['url'],True)
        filename=song['name']+'.mp3'
        mp3=urllib2.urlopen(song['url']).read()
        File=open(download_path+folder+'\\'+filename,"wb")
        File.write(mp3)
        File.close()
        log("download "+filename+" ok",True)

def create_folder():
    folder=time.strftime("%Y%m%d_%H%M%S", time.localtime())
    os.makedirs(download_path+folder)
    return folder

def log(string,console):
    File=open(project_path+'openchannel_download.log',"ab")
    timenow=time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
    File.write(timenow+" "+string.encode("utf-8")+'\n')    
    if console: print timenow,string
    File.close()

def main():
    url_data=build_search_url(keyword,cate,limit)
    songs=get_songs(url,url_data,cookie)
    download(songs)

if __name__=='__main__':
    main()
