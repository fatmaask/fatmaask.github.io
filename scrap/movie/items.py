# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    movie_id= scrapy.Field()
    rating = scrapy.Field()
    production = scrapy.Field()
    year = scrapy.Field()
    genre = scrapy.Field()
    director = scrapy.Field()
    image = scrapy.Field()
