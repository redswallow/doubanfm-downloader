from douban_client import DoubanClient
import urllib2

KEY = '0f810ec59db43e592e832c50d91cbb0b'
SECRET = '3ed567125a1335da'
SCOPE = 'douban_basic_common,shuo_basic_r,shuo_basic_w,community_basic_photo,community_advanced_doumail_r,music_basic_r'
CALLBACK='http://douban.com'
#TOKEN=''
TOKEN='b5defae9fe5aceb4219cf0bdfb106c1c'

def get_client():
    client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)

    token = TOKEN

    if token:
        client.auth_with_token(token) 
    else:
        print 'Go to the following link in your browser:' 
        print client.authorize_url

        code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
        client.auth_with_code(code)
        print client.client.token
    return client

client = get_client()
#ret =  client.user.me
ret= client.user.follow_in_common(id='46857465',start=0,count=20)
#client.user.friendships(target_id='46857465')
print ret
