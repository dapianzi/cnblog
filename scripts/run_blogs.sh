#!/bin/sh
# source /root/.bashrc
# 导入环境变量
. ~/.bash_profile

echo "*****crontab begin:*****"
cd /var/www/django-web/blog/cnblogs
#/usr/local/bin/scrapy crawl cnblogs -s LOG_FILE=/tmp/scrapy.log >> /tmp/crawl_blog.log & 
/usr/local/bin/scrapy crawl cnblogs >> /tmp/crawl_blog.log & 
echo $(ps -ef | grep "scrapy crawl cnblogs"  |grep -v 'grep' |awk -F ' ' '{print $2}')
