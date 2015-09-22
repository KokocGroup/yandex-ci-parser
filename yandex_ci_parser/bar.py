# -*-coding: utf-8 -*-
import re
from yandex_ci_parser.util import get_domain


class BarCi(object):
    base_url = 'http://bar-navig.yandex.ru/u?show=31&url=http://{domain}/'

    @classmethod
    def get_url(cls, site):
        return cls.base_url.format(domain=get_domain(site))

    @classmethod
    def _get_bar_value(cls, regexp, content):
        result = ''
        match_part = re.findall(regexp, content, re.S | re.I | re.U | re.M)
        if match_part:
            result = match_part[0].strip()

        return result

    @classmethod
    def result(cls, content):
        params = {
            'domain': ur'domain="(.*?)"',
            'title': ur'title="(.*?)"',
            'value': ur'value="(.*?)"',
            'rang': ur'rang="(.*?)"',
            'textinfo': ur'<textinfo>(.*?)</textinfo>',
            'url': ur'<topic[^>]+title[^>]+url="(.*?)"'
        }

        result = {}
        for key, regexp in params.items():
            result[key] = cls._get_bar_value(regexp, content)
            if key == 'value':
                result[key] = int(result[key])

        return result