# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'https://lightsandparts.com/product-category/led-pot-ceiling-lights/led-retrofit/',
    ]

    def parse(self, response):
        for quote in response.css("#primary > div.woocommerce.columns-4 > div"):
            yield {
                'text': quote.css("h3 > a::text").extract_first(),
                'code': quote.css("div > div.meta-wrapper > span::text").extract_first(),
                'image': quote.css("figure > img  figure > img::attr(src)").extract()
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

