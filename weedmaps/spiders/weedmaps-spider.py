# -*- coding: utf-8 -*-

import scrapy
import re
from weedmaps.items import WeedmapsItem
import datetime
import json

class WeedmapsSpider(scrapy.Spider):
    name = "weedmaps"
    
    start_urls = ["https://api-v2.weedmaps.com/api/v2/brands?page=1&page_size=150&sort_by=name&sort_order=asc"]
    
    def parse(self, response):
        
        current_page = re.search( r'page=(\d+)', response.url ).group(1)
        
        j = json.loads(response.body_as_unicode())
        
        for brand in j["data"]["brands"]:
            
            brand_url = "https://api-v2.weedmaps.com/api/v2/brands/{0}?include%5B%5D=brand.categories&include%5B%5D=brand.social".format( brand["slug"] )
            
            yield scrapy.Request( url=brand_url, callback=self.parse_brand )
        
        total_brands = j["meta"]["total_brands"]

        if ( int(current_page) * 150 < int(total_brands) ):
            next_page = int(current_page) + 1
            next_page_url = re.sub( r'page=\d+', "page={0}".format(next_page), response.url )
            
            yield scrapy.Request( url=next_page_url, callback=self.parse )
    
    def parse_brand(self, response):
        
        j = json.loads(response.body_as_unicode())
        
        for category in j['data']['brand']['categories']:
            
            for product in category['products']:
                
                item = WeedmapsItem()
                
                item["BrandTitle"] = j['data']['brand']['name']
                item["BrandPictureLink"] = j['data']['brand']['avatar_image']['large_url']
                item["BrandDescription"] = j['data']['brand']['description']
                
                item["CategoryTitle"] = category['name']
                
                item["ProductTitle"] = product['name']
                item["ProductPictureLink"] = product['avatar_image']['large_url']
                item["ProductThcContent"] = None
                item["ProductCbdContent"] = None
                item["ProductDescription"] = product['description']
                item["ProductURL"] = product['web_url']

                yield item

