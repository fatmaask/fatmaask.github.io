# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items
from scrapy import log, Request

class MovieSpider(CrawlSpider):
    name = "imdb_movies"
    allowed_domains = ["imdb.com"]
    start_urls = ['http://www.imdb.com/chart/top']


    rules = [Rule(LinkExtractor(allow=['/title/']), 'parse_page')]
    def parse_page(self, response):
        item = items.MovieItem()
        item['movie_id'] = response.url.split("/")[4]
        item['url'] = response.url
        item['name'] = response.xpath("//*[@id='overview-top']/h1/span[1]/text()")[0].extract().encode("utf-8")
        item['rating'] = response.xpath("//*[@id='overview-top']/div[3]/div[3]/strong/span[@itemprop='ratingValue']/text()")[0].extract()
        return item
