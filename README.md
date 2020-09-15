## Scrapy Zenscrape Middleware

### Acknowledgements

Thanks to [arimbr](https://github.com/arimbr) and [ScrapingBee](https://github.com/ScrapingBee/scrapy-scrapingbee), this is adaptation of their work.

### Installation

`pip install scrapy-zenscrape`

### Configuration

Add your `ZENSCRAPE_API_KEY` and the `ZenscrapeMiddleware` to your project settings.py. Don't forget to set `CONCURRENT_REQUESTS` according to your [Zenscrape plan](https://zenscrape.com/#pricingSection).

```python
ZENSCRAPE_API_KEY = 'REPLACE-WITH-YOUR-API-KEY'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_zenscrape.ZenscrapeMiddleware': 700,
}

CONCURRENT_REQUESTS = 1
```

### Usage

Inherit your spiders from `ZenscrapeSpider` and yield a `ZenscrapeRequest`.

Below you can see an example from the spider in [httpbin.py](examples/httpbin/httpbin/spiders/httpbin.py).

```python
from scrapy import Spider
from scrapy_zenscrape import ZenscrapeSpider, ZenscrapeRequest

class HttpbinSpider(Spider):
    name = 'httpbin'
    start_urls = [
        'https://httpbin.org',
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
            },
            headers={
                # 'Accept-Language': 'En-US',
            },
            cookies={
                # 'name_1': 'value_1',
            })

    def parse(self, response):
        ...
```

You can pass [Zenscrape parameters](https://app.zenscrape.com/documentation) in the params argument of a ZenscrapeRequest. Headers and cookies are passed like a normal Scrapy Request. ZenscrapeRequests formats all parameters, headers and cookies to the format expected by the API.

### Examples

Add your API key to [settings.py](examples/httpbin/httpbin/settings.py).

To run the examples you need to clone this repository. In your terminal, go to `examples/httpbin/httpbin` and run the example spider with:

```bash
scrapy crawl httpbin
```
