# -*-coding: utf-8 -*-

# Парсим картинку для случая: https://yaca.yandex.ru/yca/cy/ch/apartlux.ru/
class Image(object):
    base_url = 'https://yandex.ru/cycounter?http://{domain}/'

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
    def result(cls, content):
        pass