#########################################################################
# File Name: rebotparsertest.py
# Author: pchwu
#########################################################################

#!/use/bin/python
#coding=utf-8

import urlparse
import robotparser

rp = robotparser.RobotFileParser()
#rp.set_url('http://example.webscraping.com/robots.txt')
rp.set_url(urlparse.urljoin('http://www.baidu.com','robots.txt'))
rp.read()
#url = 'http://example.webscraping.com'
url = 'http://www.baidu.com'
user_agent = 'BadCrawler'
print rp.can_fetch(user_agent, url)
user_agent = 'Baiduspider'
print rp.can_fetch(user_agent, url)
