# -*- coding: utf-8 -*-
import scrapy

IMGS_HOST = "http://www.alerj.rj.gov.br"

class AlerjSpider(scrapy.Spider):
    name = "alerj"
    start_urls = [
        "http://www.alerj.rj.gov.br/Deputados/QuemSao"
    ]
      
    def parse(self, response):
        imgs = response.css("div.imagem a img")

        data = []
        for img in response.css("div.imagem a img"):
            yield {
                "nome": img.css("::attr(alt)").extract()[0],
                "img_url": "%s%s" % (IMGS_HOST, img.css("::attr(src)").extract()[0])
            }
