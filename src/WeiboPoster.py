#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.2'
__author__ = 'Matthew (matthewgao@gmail.com)'

from weibo import APIClient
import urllib2,urllib

class WeiboPoster:
    def __init__(self):
        self.APP_KEY = '2814174092'
        self.APP_SECRET = 'bd036add6f75fe4714c935a4f94443dd'
        self.CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
        self.AUTH_URL = 'https://api.weibo.com/oauth2/authorize'

        self.client = APIClient(app_key=self.APP_KEY, \
                                app_secret=self.APP_SECRET, \
                                redirect_uri=self.CALLBACK_URL)
        
        url = self.client.get_authorize_url()

        postdata = {
            "action": "login",
            "client_id": self.APP_KEY,
            "redirect_uri":self.CALLBACK_URL,
            "userId": "username",
            "passwd": "password",
            }

        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0",
            "Referer":url,
            "Connection":"keep-alive"
        }
        req  = urllib2.Request(
            url = self.AUTH_URL,
            data = urllib.urlencode(postdata),
            headers = headers
        )
        resp = urllib2.urlopen(req)
        code = resp.geturl()[-32:]
        
        r = self.client.request_access_token(code)
        access_token = r.access_token
        expires_in = r.expires_in
        self.client.set_access_token(access_token, expires_in)

    def postWeibo(self,text):
        utext = unicode(text, "UTF-8")
        self.client.statuses.update.post(status=utext)
        
    def postWeiboWithImage(self,text,img):
        utext = unicode(text, "UTF-8")
        self.client.statuses.upload.post(status=utext,pic=img)

    '''
    def postWeiboWithImageAndPos(self,text,img,lat,long):
        utext = unicode(text, "UTF-8")
        self.client.statuses.update.post(status=utext,pic=img,)
    '''
