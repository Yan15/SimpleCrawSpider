# coding:utf-8
import urllib2
class HtmlDownloader:
    def download(self,url):
        if url is None:
            return
        response = urllib2.urlopen(url)
        if response.code != 200:
            return
        return response.read()