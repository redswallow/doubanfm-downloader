#coding=utf-8
from urllib import urlencode
import urllib,urllib2,cookielib,re,os

#config
username='redswallowjysc@126.com'
password='901212jysc'
logurl='https://www.douban.com/accounts/login'


def check_url(url,operate):
    if url=='http://www.douban.com/':
        print 'Logged on successfully!'
        return True
    elif url=='https://www.douban.com/accounts/login':
        read_captcha(operate.read())
    else:
        print 'Logged on error'
        return False

def read_captcha(html):
    imgurl=re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url=imgurl.group(1)
        res=urllib.urlretrieve(url, 'v.jpg')
        captcha=re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>' ,html)
        if captcha:
            vcode=raw_input('captcha:')
            params={"form_email":username,
                "form_password":password,
                "source":"index_nav",
                "captcha-solution":vcode,
                "captcha-id":captcha.group(1),
                "user_login":"登录"
            }
            login_params(params)

def login():
    params={"form_email":username,
            "form_password":password,
            "source":"index_nav"
    }
    login_params(params)

def login_params(params):
    #cookie
    cj=cookielib.LWPCookieJar()
    if os.path.isfile('douban.cookie'):
        cj.load('douban.cookie')
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    url_data=urlencode(params)
    req=urllib2.Request(logurl,url_data)
    operate=opener.open(req)
    if check_url(operate.geturl(),operate):
        cj.save('douban.cookie')

if __name__=='__main__':
    login()
