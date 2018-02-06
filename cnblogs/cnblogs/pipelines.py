# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import re
import time
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request


class CnblogsPipeline(object):
    """Save item to mysql"""

    def process_item(self, item, spider):
        # save item
        spider.cursor.execute("SELECT id FROM app_article WHERE title=%s", (item['title'], ))
        if spider.cursor.fetchone():
            raise DropItem('Article already existes.')
        sql = "INSERT INTO app_article (title, md_body, pub_time, from_url, author_id, category_id) VALUES (%s, %s, %s, %s, %s, %s)"
        spider.cursor.execute(sql, (item['title'], item['body'], item['pub_time'], item['link'], 1, 1))
        spider.db.commit()
        a_id = spider.cursor.lastrowid
        # handle tags and category
        # print(item['tags'])
        for tag in item['tags']:
            spider.cursor.execute("SELECT id FROM app_tags WHERE name=%s", (tag,))
            tag_id = spider.cursor.fetchone()
            if not tag_id:
                spider.cursor.execute("INSERT INTO app_tags (name) VALUES (%s)", (tag,))
                spider.db.commit()
                tag_id = spider.cursor.lastrowid
            sql = "INSERT INTO app_article_tags (article_id,tags_id) VALUES (%s, %s) "
            spider.cursor.execute(sql, (a_id, tag_id))
            spider.db.commit()
        return item

class ImgsPipeline(ImagesPipeline):
    """Download images"""

    def get_media_requests(self, item, info):
        # build request referer
        for i in item['imgs']:
            yield Request(i, headers={"Referer": item['link']})

    def item_completed(self, results, item, info):
        for ok, x in results:
            if not ok:
                raise DropItem("Item contains no files")
            # 根据实际文件url地址
            item['body'] = item['body'].replace(x['url'], '/data/'+x['path'])
        return item
