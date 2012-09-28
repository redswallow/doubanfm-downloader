# coding=utf-8
from urllib import urlencode
import urllib,urllib2,cookielib,json,time,os
import openchannel_download

#config 
bubbler_url='http://bubbler.labs.douban.com/j/wall/'
user='redswallow'
#album_id='86'

def get_board_list(url,user):
    #build request
    content=urllib2.urlopen(url+user).read()
    dict=json.loads(content)
    #get songs
    board=dict["board_list"]
    return board

def get_board(board_list,id=0,index=0):
    if id!=0:
        for board in board_list:
            if str(id)==board["id"]: return board
    else:
        return board_list[index]

def get_songs(board):
    return board["song_list"]

board_list=get_board_list(bubbler_url,user)
board=get_board(board_list,index=1)
songs=get_songs(board)
for id in songs:
    url_data=openchannel_download.build_search_url(id)
    songs=openchannel_download.get_songs(openchannel_download.url,url_data,openchannel_download.cookie)
    print songs
