# -*- coding: utf-8 -*-
from scrapy_zenscrape import ZenscrapeRequest
from scrapy import Spider
from httpbin.items import HttpbinItem


class HttpbinSpider(Spider):
    name = 'httpbin'
    start_urls = [
        'https://httpbin.org',
        'https://httpbin.org/headers?json',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield ZenscrapeRequest(url, params={
                # 'render': False,
                # 'block_ads': True,
                # 'block_resources': False,
                # 'premium': True,
                # 'location': 'fr',
                # 'wait_for': 5,
                # 'wait_for_css': '#swagger-ui',
            }, headers={
                # 'Accept-Language': 'En-US',
            }, cookies={
                # 'name_1': 'value_1',
            })

    def parse(self, response):
        body = response.body.decode(response.encoding)
        return HttpbinItem(
            url=response.url,
            status=response.status,
            body=body,
            headers=response.headers,
        )
