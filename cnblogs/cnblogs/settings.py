# -*- coding: utf-8 -*-

# Scrapy settings for cnblogs project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'cnblogs'

SPIDER_MODULES = ['cnblogs.spiders']
NEWSPIDER_MODULE = 'cnblogs.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cnblogs (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml,*/*',
    'Accept-Language': 'zh-CN',
    'Accept-Encoding': 'gzip, deflate',

}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'cnblogs.middlewares.CnblogsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'cnblogs.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'cnblogs.pipelines.ImgsPipeline': 100,
   'cnblogs.pipelines.CnblogsPipeline': 300,
}
# image store dir
# IMAGES_STORE = '/var/www/data/'
IMAGES_STORE = '../data/'
# image thumb size
# IMAGES_THUMBS = {
#     'small': (90, 90),
# }
# image filter size
# IMAGES_MIN_HEIGHT = 120
# IMAGES_MIN_WIDTH = 120
# redirect download url
MEDIA_ALLOW_REDIRECTS = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# MYSQL CONFIG
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASS = '********'
MYSQL_NAME = 'blog'

# COOKIE
COOKIE = {
    '.CNBlogsCookie': 'B4A3B259FFBE3F24C8734BB2AA6E24AE8DBD13FD3997C49D8BF7F79C897970FFBD31C10283CBAF54C432508C42A0AF1844C40945093FAF1A21533C590091A2EFA317D71745C3AD602F4A90312747E6328AA7642D',
    '.Cnblogs.AspNetCore.Cookies': 'CfDJ8N7AeFYNSk1Put6Iydpme2bjkHk-JAyZTc72jPwfkBPSuU8GxubeXuTB4m7J138gLxQuSL5G7lSb3sbhIn_r5mrvZzdQX9oQfAEqFO4_Mye9h4AUY38yIhDp2Cc3MEewzkwfQjFx1PmiTzmHlTKPnNK0TexqOTTXFs8aiUneGt1aOzapLHazEEkZJvbGasXX-gdBS_3wdOMtXqF9h-622dwqijJOqzJMqHIuE9lnyquifXA_uYnO12u7EJhN1wFpgXdOXP8B1_Lxs_bNz0NO_o1oi4gwsMd8Q0xTLt42PKUuoXb1uVu99r4VTAMQpDcjZA',
    'AJSTAT_ok_times': '3',
    'CNZZDATA1252961619': '698077167-1505897770-https%253A%252F%252Fwww.baidu.com%252F%7C1505897770',
    'CNZZDATA1253667200': '279874767-1512523419-https%253A%252F%252Fwww.baidu.com%252F%7C1512523419',
    'CNZZDATA1255738818': '554585418-1511323150-https%253A%252F%252Fwww.baidu.com%252F%7C1515728731',
    'CNZZDATA1257902762': '1655581372-1513591319-https%253A%252F%252Fwww.baidu.com%252F%7C1513591319',
    'CNZZDATA1258637387': '825797014-1510293992-https%253A%252F%252Fwww.baidu.com%252F%7C1510293992',
    'CNZZDATA1258934647': '645127045-1501474115-https%253A%252F%252Fwww.baidu.com%252F%7C1501474115',
    'CNZZDATA1261593843': '402370633-1501474113-https%253A%252F%252Fwww.baidu.com%252F%7C1501474113',
    'CNZZDATA1263394805': '1622305713-1510124879-https%253A%252F%252Fwww.baidu.com%252F%7C1510124879',
    'CNZZDATA3347352': 'cnzz_eid%3D1278998867-1505697664-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1509415073',
    'CNZZDATA3980738': 'cnzz_eid%3D1309447145-1503992945-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1503992945',
    'CNZZDATA4343144': 'cnzz_eid%3D1303673756-1503483365-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1504852852',
    'CNZZDATA4606621': 'cnzz_eid%3D987861400-1512975841-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1516769291',
    'Hm_lvt_0ba2040c6872271f07fcbf62884d6d58': '1492142866',
    'Hm_lvt_674430fbddd66a488580ec86aba288f7': '1503483347,1504852847',
    'Hm_lvt_983ff56c7e2c7f4ebd3fbe17d812b05e': '1500345192',
    'UM_distinctid': '15e9e804c9a53e-0820ac933127b3-e313761-13c680-15e9e804c9bafb',
    '__gads': 'ID',
    '__utma': '226521935.1530423021.1490067516.1514282116.1514363733.9',
    '__utmz': '226521935.1514363733.9.4.utmcsr',
    '_ga': 'GA1.2.1530423021.1490067516',
    '_gat': '1',
    '_gid': 'GA1.2.1246087160.1516940901',
    'lhb_smart_1': '1',
    'pgv_pvi': '6307338240',
    'sc_is_visitor_unique': 'rx9614694.1505120825.1C89AF7968144F8BBCA8B29DB72C146D.1.1.1.1.1.1.1.1.1',
}
