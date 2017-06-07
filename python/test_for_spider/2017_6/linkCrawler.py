#########################################################################
# File Name: linkCrawler.py
# Author: pchwu
#########################################################################

#!/use/bin/python
#coding=utf-8

import urlparse
import downloadUrl
import re

def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)

    while crawl_queue:
        url = crawl_queue.pop()
        html = downloadUrl.download(url)
        for link in get_links(html):
            if re.search(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)
    return crawl_queue

def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

if __name__ == "__main__":
    print link_crawler("http://example.webscraping.com", '/(index|view)')
