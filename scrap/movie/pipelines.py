# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DBWritePipeline(object):
    def process_item(self, item, spider):
        return item
