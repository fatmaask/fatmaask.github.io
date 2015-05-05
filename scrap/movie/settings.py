# -*- coding: utf-8 -*-

# Scrapy settings for altyazi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'movie'

SPIDER_MODULES = ['movie.spiders']
NEWSPIDER_MODULE = 'movie.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'CENG Web Mining Course DemoSpider'

DOWNLOAD_DELAY = 1
HTTPCACHE_ENABLED = True
