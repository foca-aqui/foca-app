# -*- coding: utf-8 -*-
import scrapy

IMGS_HOST = "http://www.alerj.rj.gov.br"

class AlerjSpider(scrapy.Spider):
    name = "alerj"
    start_urls = [
        "http://www.alerj.rj.gov.br/Deputados/QuemSao"
    ]
    
    def parse_detail(self, response):
        obj = response.request.meta

        size = len(response.css("div.descricao p::text").extract())
        tel = response.css("div.descricao p::text").extract()[size-2]
        email = response.css("div.descricao p::text").extract()[size-1]
        
        yield {
            "nome": obj["nome"],
            "img_url": obj["img_url"],
            "telefone": tel,
            "email": email
        }

    def parse(self, response):
        for img in response.css("div.imagem"):
            detail_page = "%s%s" % (IMGS_HOST, img.css("a::attr(href)").extract()[0])
            
            if len(img.css("a img::attr(alt)").extract()) > 0:
                obj = {
                    "nome": img.css("a img::attr(alt)").extract()[0],
                    "img_url": "%s%s" % (IMGS_HOST, img.css("a img::attr(src)").extract()[0])
                }
                
                yield scrapy.Request(
                    detail_page, 
                    callback=self.parse_detail,
                    meta=obj
                )
