# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://lightsandparts.com/products/',
    ]

    def parse(self, response):
        for quote in response.css("div.vc_row"):
            yield {
                'text': quote.css("h3 > a > span::text").extract_first(),
                'image': quote.css("figure > a > img::attr(src)").extract()
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

