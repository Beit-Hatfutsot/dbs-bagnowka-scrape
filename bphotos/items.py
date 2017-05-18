# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BphotosItem(scrapy.Item):
    gallery_name = scrapy.Field()
    photo_title = scrapy.Field()
    date = scrapy.Field()
    description_today = scrapy.Field()
    photographer = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
