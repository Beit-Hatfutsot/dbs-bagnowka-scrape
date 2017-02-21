# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Photo(scrapy.Item):
    # define the fields for your item here like:
    #gallery_name = scrapy.Field()
    #photo_name = scrapy.Field()
    #date = scrapy.Field()
    #description_today = scrapy.Field()
    #photographer = scrapy.Field()
    img_url = scrapy.Field()
    inner_url = scrapy.Field()
