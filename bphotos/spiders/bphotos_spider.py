# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy import Request
from bphotos.items import BphotosItem

'''
Using Scrapy to scrape www.bagnowka.pl to get all photos and data from "A-Z Gallry".
Images are uploaded to images to AWS s3
Access keys in "settings.py" should be replaced with valid keys
'''

class BphotosSpider(CrawlSpider):
    name = 'bphotos'
    allowed_domains = ['bagnowka.pl']
    start_urls = ['http://www.bagnowka.pl/index.php?m=atoz&l=16',
                'http://www.bagnowka.pl/index.php?m=atoz&l=17',
                'http://www.bagnowka.pl/index.php?m=atoz&l=18',
                'http://www.bagnowka.pl/index.php?m=atoz&l=19',
                'http://www.bagnowka.pl/index.php?m=atoz&l=20',
                'http://www.bagnowka.pl/index.php?m=atoz&l=21',
                'http://www.bagnowka.pl/index.php?m=atoz&l=22',
                'http://www.bagnowka.pl/index.php?m=atoz&l=23',
                'http://www.bagnowka.pl/index.php?m=atoz&l=24',
                'http://www.bagnowka.pl/index.php?m=atoz&l=25',
                'http://www.bagnowka.pl/index.php?m=atoz&l=26',
                'http://www.bagnowka.pl/index.php?m=atoz&l=27',
                'http://www.bagnowka.pl/index.php?m=atoz&l=28',
                'http://www.bagnowka.pl/index.php?m=atoz&l=29',
                'http://www.bagnowka.pl/index.php?m=atoz&l=30',
                'http://www.bagnowka.pl/index.php?m=atoz&l=31',
                'http://www.bagnowka.pl/index.php?m=atoz&l=32',
                'http://www.bagnowka.pl/index.php?m=atoz&l=33',
                'http://www.bagnowka.pl/index.php?m=atoz&l=34',
                'http://www.bagnowka.pl/index.php?m=atoz&l=35',
                'http://www.bagnowka.pl/index.php?m=atoz&l=36',
                'http://www.bagnowka.pl/index.php?m=atoz&l=37',
                'http://www.bagnowka.pl/index.php?m=atoz&l=38',
                'http://www.bagnowka.pl/index.php?m=atoz&l=39',
                'http://www.bagnowka.pl/index.php?m=atoz&l=40',
                'http://www.bagnowka.pl/index.php?m=atoz&l=41'
                ]

    def parse(self, response):
        # Extract galleries
        base_url = 'http://www.bagnowka.pl/index.php/'
        for lin in response.xpath('//tr/td/a[contains(@href, "?m=atoz&pod")]/@href').extract():
            lin = "{}{}".format(base_url, str(lin))
            yield Request(lin, callback=self.parse)
        for link in response.xpath('//tr/td/a[contains(@href, "?m=atoz&g=")]/@href').extract():
            link = "{}{}".format(base_url, str(link))
            yield Request(link, callback=self.parse_galleries)
            # Extract inner galleries and send them back to be parsed for
            # galleries

    def parse_galleries(self, response):
        base_url = 'http://www.bagnowka.pl/index.php/'
        photo = response.xpath(
            '//tr/td/a[contains(@href, "m=atoz&g=1&img=")]/@href').extract_first()
        photo = "{}{}".format(base_url, str(photo))
        yield Request(photo, callback=self.parse_p)


    def parse_p(self, response):
        base_url = 'http://www.bagnowka.pl/'
        image_urls = [response.xpath('//tr/td[2]/div/img/@src').extract_first()]
        photo = BphotosItem()
        photo["gallery_name"] = response.xpath(
            '//tr/td[4]/span/b/text()').extract_first(),
        photo["photo_title"] = response.xpath(
            '//tr/td[4]/b[5]/text()').extract_first(),
        photo["date"] = response.xpath(
            '//tr/td[4]/text()')[3].extract().rstrip(),
        photo["description_today"] = response.xpath(
            '//tr/td[4]/text()')[2].extract().rstrip(),
        photo["photographer"] = response.xpath(
            '//tr/td[4]/text()[5]').extract_first(),
        photo["image_urls"] = [base_url + str(x) for x in image_urls]
        yield photo

        next_page = response.xpath(
            '//tr/td[2]/div/span/a[contains(text(), "Next")]/@href').extract_first()
        if next_page is not None:
            next_page = "{}{}".format(base_url, str(next_page))
            yield Request(next_page, callback=self.parse_p)
