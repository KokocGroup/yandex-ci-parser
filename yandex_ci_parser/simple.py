# -*-coding: utf-8 -*-

import requests
from yandex_ci_parser.errors import IncorrectParserError


class SimpleCi(object):

    @classmethod
    def get_bar(cls, site):
        from yandex_ci_parser.bar import BarCi
        url = BarCi.get_url(site)
        res = requests.get(url)
        res.raise_for_status()
        return BarCi.result(res.text)

    @classmethod
    def get_yaca(cls, site):
        from yandex_ci_parser.yaca import YacaCi
        url = YacaCi.get_url(site)
        res = requests.get(url)
        res.raise_for_status()
        return YacaCi.result(res.text, site)

    @classmethod
    def get_image(cls, site):
        from yandex_ci_parser.image import ImageCi
        url = ImageCi.get_url(site)
        res = requests.get(url)
        res.raise_for_status()
        return ImageCi.result(res.text)

    @classmethod
    def get_yaca_image(cls, site):
        from yandex_ci_parser.yaca import YacaCi

        url = YacaCi.get_url(site)
        res = requests.get(url)
        res.raise_for_status()
        try:
            ci = YacaCi.result(res.text, site)
        except IncorrectParserError:
            from yandex_ci_parser.image import ImageCi

            url = ImageCi.get_url(site)
            res = requests.get(url)
            res.raise_for_status()
            ci = ImageCi.result(res.content)

        return ci