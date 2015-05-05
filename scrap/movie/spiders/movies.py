# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items
from scrapy import log, Request

class MovieSpider(CrawlSpider):
    name = "movies"
    allowed_domains = ["sinemalar.com"]
    start_urls = (
        'http://www.sinemalar.com/kullanici/fatmaasik33/izledikleri/filmler/%s' % page for page in xrange(1,15)
    )
    # http://www.sinemalar.com/film/638/esaretin-bedeli
    rules = [Rule(LinkExtractor(allow=['/film/']), 'parse_page')]
    def parse_page(self, response):
        item = items.MovieItem()
        item['movie_id'] = response.url.split("/")[4]
        item['url'] = response.url
        item['name'] = response.xpath("//*[@id='container']/div[3]/hgroup//span/text()").extract()
        """if(len(response.xpath("//*[@id='container']/div[3]/hgroup/h2/small/span/text()").extract())<1):
            item['name']=response.xpath("//*[@id='container']/div[3]/hgroup/h1/span/text()").extract()[0]"""
        #item['name'].append(response.xpath("//*[@id='container']/div[3]/hgroup/h1/span/text()").extract())
        item['rating'] = response.xpath("//*[@id='rating']/text()")[0].extract().encode("utf-8")
        item['production']= response.xpath("//*[@id='container']/div[3]/div[3]/article[1]/div/div[2]/p/span/a[2]/text()")[0].extract().encode("utf-8")
        item['year']= response.xpath("//*[@id='container']/div[3]/div[3]/article[1]/div/div[2]/p/span/a[1]/text()")[0].extract()
        item['genre']= response.xpath("//*[@id='container']/div[3]/div[3]/article[1]/div/div[2]/p/span//span[@itemprop='genre']/text()").extract()
        """genres=[]
        for i in item['genre']:
            genre=i.encode('utf-8')
            genres.append(genre)
            item['genre']= ",".join(str(bit) for bit in genres)"""
        item['director']= response.xpath("//*[@id='container']/div[3]/div[3]/article[1]/div/div[2]/p/span[@itemprop='director']/a/span/text()").extract()
        """directors=[]
        for i in item['director']:
            director=i.encode('utf-8')
            directors.append(director)
            item['director']= ",".join(str(bit) for bit in directors)"""
        item['image'] = response.xpath("//*[@id='container']/div[3]/div[3]/article[1]/div/div[1]/a[1]/img/@src").extract()
        return item
