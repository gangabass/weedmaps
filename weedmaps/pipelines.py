# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.exporters import CsvItemExporter
import re

class WeedmapsPipeline(object):
    def __init__(self):
        self.exporters = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        
        spider_name = re.sub('-.+?$', '', spider.name)
        self.filename = spider_name + ".csv"
        
        file = open('output/' + self.filename, 'w+b', 0)
        exporter = CsvItemExporter(file)
        
        EXPORT_FIELDS = [
            'BrandTitle',
            'BrandPictureLink',
            'BrandDescription',
            'CategoryTitle',
            'CategoryPictureLink',
            'CategoryDescription',
            'ProductTitle',
            'ProductPictureLink',
            'ProductThcContent',
            'ProductCbdContent',
            'ProductDescription',
            'ProductURL',      
        ]
                
        exporter.fields_to_export = EXPORT_FIELDS
        exporter.start_exporting()

        self.exporters['Result'] = exporter

    def spider_closed(self, spider):
        for exporter in self.exporters.itervalues(): 
            exporter.finish_exporting()

    def process_item(self, item, spider):

        self.exporters['Result'].export_item(item)
        return item

