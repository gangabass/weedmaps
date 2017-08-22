# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

def clear(value):
    
    if value is None:
        value = ""
    
    value = value.strip()
    return value

class WeedmapsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field(serializer=clear)
    
    BrandTitle = scrapy.Field(serializer=clear)
    BrandPictureLink = scrapy.Field(serializer=clear)
    BrandDescription = scrapy.Field(serializer=clear)
    CategoryTitle = scrapy.Field(serializer=clear)
    CategoryPictureLink = scrapy.Field(serializer=clear)
    CategoryDescription = scrapy.Field(serializer=clear)
    ProductTitle = scrapy.Field(serializer=clear)
    ProductPictureLink = scrapy.Field(serializer=clear)
    ProductThcContent = scrapy.Field(serializer=clear)
    ProductCbdContent = scrapy.Field(serializer=clear)
    ProductDescription = scrapy.Field(serializer=clear)
    
    ProductURL = scrapy.Field(serializer=clear)
                                
    URL = scrapy.Field()
    pass
