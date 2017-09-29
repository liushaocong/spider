# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from twisted.enterprise import adbapi



class TutorialPipeline(object):
#     def __init__(self):
#         self.f = open("daomu.json","wb+")
#
#     def process_item(self, item, spider):
#         content = json.dumps(dict(item),ensure_ascii = False) + ",\n"
#         self.f.write(content.encode("utf-8"))
#         return item
#     # 返回引擎
#     def close_spider(self,spider):
#         self.f.close()
    def process_item(self, item, spider):
        connect = pymysql.connect(  # 连接数据库
            user="root",
            password="cong0213",
            host="127.0.0.1",
            db="scrapys",
            port=3306,
            charset=("utf8"),  # 注意编码一定要设置，否则gbk你懂的
            use_unicode=True,
        )
        con = connect.cursor()  # 设置游标
        # con.execute('SET NAMES UTF8')
        con.execute("use scrapys")  # 使用douban这个数据库
        con.execute("insert into jsbooks(title,body)values(%s,%s)",
                    [item['title'],item['body']])
        # con.execute("insert into hrefs(href,title)values(%s,%s)",
        #             [item['href'],item['title']])
        connect.commit()   #我们需要提交数据库，否则数据还是不能上传的
        con.close()   #关闭游标
        connect.close()  #关闭数据库

        return item

