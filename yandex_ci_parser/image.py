# -*-coding: utf-8 -*-

import re
from yandex_ci_parser.util import get_domain


class ImageCi(object):
    base_url = 'https://yandex.ru/cycounter?http://{domain}/'

    @classmethod
    def get_url(cls, site):
        return cls.base_url.format(domain=get_domain(site))

    @classmethod
    def result(cls, content):
        from StringIO import StringIO
        from PIL import Image

        im = Image.open(StringIO(content)).convert('RGB')
        pixdata = im.load()
        color = pixdata[45, 28]
        for y in xrange(im.size[1]):
            for x in xrange(im.size[0]):
                if pixdata[x, y] == color:
                    pixdata[x, y] = (255, 255, 255)

        data = ''
        for x in range(21, 67):
            for y in range(2, 18):
                color = pixdata[x, y]
                data += 'B' if color[0] < 255 and color[1] < 255 and color[2] < 255 else 'T'

        patterns = {
            8: ur'..BBBBB..BBBBBB..BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB....BB.....BBBBBBBBBBBBBBBBBB.BBBBBBBBBBBBBBB...BBB...BBBBBB.',
            9: ur'..BBBBBBB...BBB..BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB.....BBB...BBBBBBBBBBBBBBBBBB.BBBBBBBBBBBBBB.....BBBBBBBB....',
            4: ur'.........BBBB.........BBBBBBB......BBBBBBB.BB.BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB...........BB.BB',
            0: ur'...BBBBBBBBBBB...BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB...........BB.BBBBBBBBBBBBBBB.BBBBBBBBBBBBBB.',
            2: ur'..BBBBB.....BBBB.BBBBBB...BBBBBBBBBBBBB.BBBBBBBBBBBB..BBBBBB..BBBBBBBBBBBB.BBBBB.BBBBBBBB..BBBBB',
            3: ur'..BBBB....BBBBB..BBBBBB...BBBBBBBBBBBB.BB.BBBBBBBBB...BBBB....BB.BBBBBBBBBBBBBBB.BBBBBBBBBBBBBBB',
            5: ur'..BBBBBBB..BBBB.BBBBBBBBB..BBBBBBBBBBBBBB..BBBBBBBB...BBB....BBBBBB...BBBBBBBBBBBBB...BBBBBBBBB.',
            6: ur'...BBBBBBBBBBB...BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB...BBB.....BBBBBBBBBBBBBBBBBB.BBBBB.BBBBBBBBB',
            7: ur'BBBBBBB.........BBBBBBB.........BBBB...BBBBBBBBBBBB.BBBBBBBBBBBBBBBBBBBBBBBB....BBBBBB..........',
            1: ur'..BB..........BB.BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB..............BB',
        }
        for num in patterns:
            data = re.sub(patterns[num], str(num), data)

        data = data.replace('B', '').replace('T', '')

        return int(data) if data else None