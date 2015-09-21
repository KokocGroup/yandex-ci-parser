# -*-coding: utf-8 -*-
import re


class Yaca(object):
    base_url = 'http://yaca.yandex.ru/yca/cy/ch/{domain}/'

    @classmethod
    def get_domain(cls, site):
        domain = site
        if '://' in site:
            from urlparse import urlparse
            o = urlparse(site)
            domain = o.hostname
        return domain

    @classmethod
    def get_url(cls, site):
        return cls.base_url.format(domain=cls.get_domain(site))

    @classmethod
    def result(cls, site, content):
        domain = cls.get_domain(site)
        # Ci unknown
        pattern = re.compile(
            ur'<a href="[^"]*{domain}[^"]*" target="_blank">[^<]*</a><div>[^<]*</div>\s*</td>\s*<td>(\d+)<\/td>'.format(
                domain=re.escape(domain)
            ), re.I | re.M | re.S)
        res = pattern.search(content)
        if res:
            return int(res.group(1))

        # is text: Индекс цитирования (тИЦ) ресурса — не определен
        pattern = re.compile(
            ur'<p class="b-cy_error-cy">\s*Индекс цитирования \(тИЦ\) ресурса —\s*не определен', re.I | re.M | re.S
        )
        res = pattern.search(content)
        if res:
            return None

        # is ci
        pattern = re.compile(
            ur'<p class="b-cy_error-cy">\s*Индекс цитирования \(тИЦ\) ресурса —\s*(\d+)', re.I | re.M | re.S
        )
        res = pattern.search(content)
        if res:
            return int(res.group(1))

        raise Exception(u'Incorrect parser')