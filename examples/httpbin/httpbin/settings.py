# -*- coding: utf-8 -*-
BOT_NAME = 'httpbin'

SPIDER_MODULES = ['httpbin.spiders']
NEWSPIDER_MODULE = 'httpbin.spiders'

ZENSCRAPE_API_KEY = 'REPLACE-WITH-YOUR-API-KEY'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_zenscrape.ZenscrapeMiddleware': 700,
}

CONCURRENT_REQUESTS = 1
