# -*- coding: utf-8 -*-
import scrapy


class SamsclubComSpider(scrapy.Spider):
    name = "samsclub.com"
    allowed_domains = ["samsclub.com"]
    start_urls = ['http://samsclub.com/']

    def parse(self, response):
        pass
