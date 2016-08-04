import url_manager,html_downloader,html_parser,html_outputer
class Spider:
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser  = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url,url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(url, html_cont)
                self.urls.add_new_urls(new_urls)
                print(new_data)
                self.outputer.collect_data(new_data)
                if count == 30:
                    break
                count +=1
            except:
                print 'Craw Failed'
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/link?url=KRgtqIOD9OwpEek9TiHRi1vwF6Hfc8WFupoAUmVK3eg-3jGOhnag4BmEzAD1Sx_sOTQQfe1QNZI3rvdOwn4H94w8Gf6UG_sDTIjo6b-U5h7"
    url = "http://baike.baidu.com"
    obj_spider = Spider()
    obj_spider.craw(root_url,url)


