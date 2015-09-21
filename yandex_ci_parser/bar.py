# -*-coding: utf-8 -*-
import re


class Bar(object):
    base_url = 'http://bar-navig.yandex.ru/u?show=31&url=http://{domain}/'

    @classmethod
    def get_url(cls, site):
        domain = site
        if '://' in site:
            from urlparse import urlparse
            o = urlparse(site)
            domain = o.hostname
        return cls.base_url.format(domain=domain)

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
        return result