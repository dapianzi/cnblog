import scrapy
import re
import time
import pymysql
from scrapy.conf import settings
from cnblogs.items import CnblogsItem

class Cnblogs(scrapy.Spider):
    name = 'cnblogs'
    page = 0
    stop = False
    last_id = 0
    curr_id = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        conf = {
            'host': settings.get('MYSQL_HOST'),
            'port': settings.get('MYSQL_PORT'),
            'name': settings.get('MYSQL_NAME'),
            'user': settings.get('MYSQL_USER'),
            'pass': settings.get('MYSQL_PASS')
        }
        try:
            self.db = pymysql.connect(conf['host'], conf['user'], conf['pass'], conf['name'], port=conf['port'],
                                      charset='utf8')
        except pymysql.OperationalError as e:
            print("Mysql Operation Error[%d]: %s" % tuple(e))
            exit(0)
        self.cursor = self.db.cursor()

        sql = "SELECT conf_int FROM app_config WHERE conf_key=%s"
        self.cursor.execute(sql, ('last_id',))
        row = self.cursor.fetchone()
        if row:
            self.last_id = int(row[0])
        else:
            self.last_id = 1
        print("=======Scrapy start with id:%d=======" % self.last_id)

    def __del__(self):
        if self.curr_id > self.last_id:
            sql = "UPDATE app_config SET conf_int=%s WHERE conf_key=%s"
            self.cursor.execute(sql, (self.curr_id, 'last_id'))
            self.db.commit()
        self.db.close()
        print("=======Scrapy finish with id:%d======" % self.curr_id)

    def start_requests(self):
        yield scrapy.Request('https://i.cnblogs.com/', cookies=settings['COOKIE'], callback=self.parse)

    def parse(self, response):
        """
        文章ID是倒序排列的，记录当前已抓取的文章id，避免重复抓取
        如果文章的发表时间跟ID顺序不一样（先存草稿再发布），会导致抓取不到
        """
        articles = response.xpath('//div[@class="postTitl2"]/a')
        for a in articles:
            res = re.findall(r'p\/(\d+)\.html', a.xpath('./@href').extract_first())
            if res:
                postid = int(res[0])
                # print(postid)
                if postid <= self.last_id:
                    self.stop = True
                    break
                if postid > self.curr_id:
                    self.curr_id = postid
                yield scrapy.Request('https://i.cnblogs.com/EditPosts.aspx?postid=%d&update=1' % postid,
                                     callback=self.parse_content, meta={'postid': postid})
        if not self.stop and self.page < 10:
            self.page += 1
            yield scrapy.Request('http://www.cnblogs.com/dapianzi/p/?page=%d' % self.page, callback=self.parse)

    def parse_content(self, response):
        # 各级 request 之间传递参数用 meta
        print("Crawl post[%d]" % response.meta['postid'])
        # self.write(response)
        title = response.xpath('//input[@id="Editor_Edit_txbTitle"]/@value').extract_first()
        body = response.xpath('//textarea[@id="Editor_Edit_EditorBody"]/text()').extract_first()
        pub_time = response.xpath('//input[@id="Editor_Edit_AdvancedPanelOther_tbPublisTime"]/@value').extract_first()
        link = response.xpath('//a[@id="Editor_Edit_hlEntryLink"]/text()').extract_first()
        tags = response.xpath('//table[@id="Editor_Edit_APOptions_Advancedpanel1_cklCategories"]//input[@checked="checked"]/following-sibling::label[1]/text()').extract()
        imgs = re.findall(r'!\[.*?\]\((.*?)\)', body, re.M|re.S|re.I)

        yield CnblogsItem(
            title=title,
            body=body + "\n*本文首次发表于[%s](%s)*" % (title, link),
            pub_time=time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(pub_time, '%m/%d/%Y %I:%M:%S %p')),
            link=link,
            tags=tags,
            imgs=imgs
        )

    def write(self, res):
        with open('temp.html', 'wb') as f:
            f.write(res.body)
