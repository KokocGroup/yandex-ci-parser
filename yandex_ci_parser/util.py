# -*-coding: utf-8 -*-


def get_domain(site):
    domain = site
    if '://' in site:
        from urlparse import urlparse
        o = urlparse(site)
        domain = o.hostname
    return domain