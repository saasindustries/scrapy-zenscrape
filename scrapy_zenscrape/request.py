import base64
import copy
import logging

from scrapy import Request
from scrapy.spidermiddlewares.httperror import HttpError

logger = logging.getLogger(__name__)


class ZenscrapeRequest(Request):

    def __init__(self, url, params={}, headers=None, body=None,
                 cookies=None, meta=None, **kwargs):
        meta = copy.deepcopy(meta) or {}

        if headers:
            params['forward_headers'] = True
            headers = self.process_headers(headers)

        params = self.process_params({
            **{'url': url},
            **{'cookies': cookies},
            **params
        })

        meta['zenscrape'] = {
            'params': params
        }

        super().__init__(
            url,
            headers=headers,
            body=body,
            meta=meta,
            errback=self.handle_error,
            **kwargs
        )

    @staticmethod
    def process_cookies(d):
        if isinstance(d, dict):
            return ';'.join(f'{k}={v}' for k, v in d.items())
        elif isinstance(d, list):
            raise NotImplementedError
        elif isinstance(d, str):
            return d

    @classmethod
    def process_params(cls, params):
        new_params = {}
        for k, v in params.items():
            if v in (None, '', [], {}):
                continue
            elif k == 'cookies':
                new_params[k] = cls.process_cookies(v)
            else:
                new_params[k] = v
        return new_params

    def handle_error(self, error):
        if error.check(HttpError):
            logger.error(
                f'Got Zenscrape error: {error.value.response.text}')
        else:
            logger.error(repr(error))
