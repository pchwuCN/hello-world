import urllib2
import re
import time 

def download(url, user_agent='wdwp', proxy=None, num_retry=2):
    print("Downloading: ", url)
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.proxyHandler(proxy_params))
    try:
        #html = urllib2.urlopen(request).read()
        html = opener.open(request).read()
        #time.sleep(0.4)
    except urllib2.URLError as e:
        print('Download error : ', e.reason)
        html = None
        if num_retry > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                html = Download(url, user_agent, proxy, num_retry-1)
                #return download(url, headers, num_retry-1)
    return html


def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<a[^>]+href=["\'](.*?)["\']', sitemap)
    #print sitemap
    for link in links:
        #html = download(link)
        print link

#print(download("http://www.baidu.com"))
download("http://www.baidu.com")
#download("http://www.meetup.com")
#download("http://httpstat.us/500", 5)
#if __name__ == "__main__":
#    print download('http://example.webscraping.com/robot.txt')
