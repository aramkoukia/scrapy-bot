# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'https://lightsandparts.com/product-category/led-pot-ceiling-lights/',
        'https://lightsandparts.com/product-category/led-pot-ceiling-lights/led-retrofit/',
        'https://lightsandparts.com/product-category/led-pot-ceiling-lights/panel-lights/',
        'https://lightsandparts.com/product-category/led-pot-ceiling-lights/surface-mount-disk-light/',
        'https://lightsandparts.com/product-category/led-pot-ceiling-lights/flush-mount/',
        'https://lightsandparts.com/product-category/cabinet-lights/',
        'https://lightsandparts.com/product-category/flexible-led-strip/',
        'https://lightsandparts.com/product-category/controllers/',
        'https://lightsandparts.com/product-category/linear-architectural-light-fixture/',
        'https://lightsandparts.com/product-category/landscape-light/',
        'https://lightsandparts.com/product-category/landscape-light/flood-light/',
        'https://lightsandparts.com/product-category/landscape-light/inground-light/',
        'https://lightsandparts.com/product-category/landscape-light/lawn-spot-light/',
        'https://lightsandparts.com/product-category/landscape-light/landscape-accessories/',
        'https://lightsandparts.com/product-category/landscape-light/outdoor-step-lights/',
        'https://lightsandparts.com/product-category/landscape-light/pathway-light/',
        'https://lightsandparts.com/product-category/landscape-light/submersible-lights/',
        'https://lightsandparts.com/product-category/landscape-light/wall-packs/',                
        'https://lightsandparts.com/product-category/landscape-light/wall-washer/',
        'https://lightsandparts.com/product-category/landscape-light/waterproof-strip-light/',
        'https://lightsandparts.com/product-category/power-supply/',
        'https://lightsandparts.com/product-category/power-supply/box/',
        'https://lightsandparts.com/product-category/power-supply/constant-current-power-supply/',
        'https://lightsandparts.com/product-category/power-supply/constant-voltage-power-supply/',
        'https://lightsandparts.com/product-category/step-lights/',
        'https://lightsandparts.com/product-category/step-lights/indoor-step-light/',
        'https://lightsandparts.com/product-category/step-lights/outdoor-step-light/',
        'https://lightsandparts.com/product-category/office-commercial-lighting/',
        'https://lightsandparts.com/product-category/elevator-lighting/',
        'https://lightsandparts.com/product-category/spot-light/',
        'https://lightsandparts.com/product-category/mr16-light-trim/',
        'https://lightsandparts.com/product-category/led-bulbs/',
        'https://lightsandparts.com/product-category/led-bulbs/a19-e26-e27/',
        'https://lightsandparts.com/product-category/led-bulbs/candelabra-bulbs/',
        'https://lightsandparts.com/product-category/led-bulbs/g4-g9-bi-pin-bulbs/',
        'https://lightsandparts.com/product-category/led-bulbs/mr16-gu10/',
        'https://lightsandparts.com/product-category/led-bulbs/par-and-br-bulbs/',
        'https://lightsandparts.com/product-category/led-bulbs/specialty-and-automotive-light/',
        'https://lightsandparts.com/product-category/led-bulbs/tube-lights/',
        'https://lightsandparts.com/product-category/led-bulbs/vintage-and-filament-bulb/',
        'https://lightsandparts.com/product-category/back-lighting/',
        'https://lightsandparts.com/product-category/back-lighting/led-module/',
        'https://lightsandparts.com/product-category/back-lighting/led-panel/',
        'https://lightsandparts.com/product-category/working-light/',
        'https://lightsandparts.com/product-category/moving-signs/',
        'https://lightsandparts.com/product-category/moving-signs/window/',
        'https://lightsandparts.com/product-category/moving-signs/window/single-color/',
        'https://lightsandparts.com/product-category/moving-signs/window/multi-color/',
        'https://lightsandparts.com/product-category/moving-signs/desktop/',
        'https://lightsandparts.com/product-category/decorative-entertainment/',
        'https://lightsandparts.com/product-category/wire-and-cabeles/',
        'https://lightsandparts.com/product-category/accessories/',
        'https://lightsandparts.com/product-category/accessories/adaptors/',
        'https://lightsandparts.com/product-category/accessories/battery/',
        'https://lightsandparts.com/product-category/accessories/box-accessories/',
        'https://lightsandparts.com/product-category/accessories/connectors/',
        'https://lightsandparts.com/product-category/accessories/diodes/',
        'https://lightsandparts.com/product-category/accessories/led-modules/',
        'https://lightsandparts.com/product-category/accessories/light-base/',
        'https://lightsandparts.com/product-category/accessories/strip-light-accessories/',
        'https://lightsandparts.com/product-category/accessories/switches/',
        'https://lightsandparts.com/product-category/accessories/waterproof-connectors/',
    ]

    def parse(self, response):
        for quote in response.xpath('//*[@id="primary"]/div[3]/div/section'):
            yield {
                'text': quote.xpath('.//h3/a/text()').extract_first(),
                'code': quote.xpath('.//div/div/span/text()').extract_first(),
                'image': quote.xpath('.//figure/img/@src').extract()
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

