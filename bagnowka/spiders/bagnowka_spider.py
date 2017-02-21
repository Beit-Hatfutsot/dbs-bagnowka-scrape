# -*- coding: utf-8 -*-


from scrapy.spiders import CrawlSpider
from scrapy import Request


class BagnowkaSpider(CrawlSpider):
    name = 'bagnowka'
    allowed_domains = ['bagnowka.pl']
    start_urls = ['http://www.bagnowka.pl/index.php?m=atoz&l=38']

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
        for link in response.xpath('//tr/td/a[contains(@href, "m=atoz&g=1&img=")]/@href').extract():
            link = "{}{}".format(base_url, str(link))
            yield Request(link, callback=self.parse_p)

            next_p = response.xpath(
                '//tr/td/a[contains(@href, "m=atoz&g=show")]/@href').extract()
            for n in next_p:
                n = "{}{}".format(base_url, str(n))
                yield Request(n, callback=self.parse_galleries)

    def parse_p(self, response):

        yield {
            "gallery_name": response.xpath(
                '//tr/td[4]/span/b/text()').extract_first(),
            #"photo_name": response.xpath(
            #   '//tr/td[4]/b[5]/text()').extract_first(),
            #"date": response.xpath('//tr/td[4]/text()')[3].extract().rstrip(),
            #"description_today": response.xpath(
            #   '//tr/td[4]/text()')[2].extract().rstrip(),
            #"photographer": response.xpath(
            #   '//tr/td[4]/text()[5]').extract_first(),
            "url": response.xpath('//tr/td[2]/div/img/@src').extract_first()
        }
