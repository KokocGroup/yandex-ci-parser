# -*-coding: utf-8 -*-

from yandex_ci_parser.tests import YandexCiParserTests
from yandex_ci_parser.bar import BarCi


class BarCiTest(YandexCiParserTests):
    def test1(self):
        content = self.get_data('bar-bdbd.ru.xml')
        res = BarCi.result(content)

        true_res = {
            'domain': 'www.bdbd.ru',
            'title': '\xd2\xe5\xec\xe0: \xcf\xf0\xee\xe4\xe2\xe8\xe6\xe5\xed\xe8\xe5 \xf1\xe0\xe9\xf2\xee\xe2',
            'url': 'http://yaca.yandex.ru/yca/',
            'rang': '5',
            'value': 1600,
            'textinfo': '\xd2\xe5\xec\xe0: \xcf\xf0\xee\xe4\xe2\xe8\xe6\xe5\xed\xe8\xe5 \xf1\xe0\xe9\xf2\xee\xe2\n\xd0\xe5\xe3\xe8\xee\xed: \xd0\xee\xf1\xf1\xe8\xff\n\xc8\xf1\xf2\xee\xf7\xed\xe8\xea: \xce\xf4\xe8\xf6\xe8\xe0\xeb\xfc\xed\xfb\xe9\n\xd1\xe5\xea\xf2\xee\xf0: \xca\xee\xec\xec\xe5\xf0\xf7\xe5\xf1\xea\xe8\xe5'
        }
        self.assertDictEqual(res, true_res)

    def test2(self):
        content = self.get_data('bar-yandex.ru.xml')
        res = BarCi.result(content)

        true_res = {
            'domain': 'www.yandex.ru',
            'title': '\xd2\xe5\xec\xe0: \xcf\xee\xe8\xf1\xea\xee\xe2\xfb\xe5 \xf1\xe8\xf1\xf2\xe5\xec\xfb',
            'url': 'http://yaca.yandex.ru/yca/',
            'rang': '6',
            'value': 500000,
            'textinfo': '\xd2\xe5\xec\xe0: \xcf\xee\xe8\xf1\xea\xee\xe2\xfb\xe5 \xf1\xe8\xf1\xf2\xe5\xec\xfb\n\xd0\xe5\xe3\xe8\xee\xed: \xd0\xee\xf1\xf1\xe8\xff\n\xc8\xf1\xf2\xee\xf7\xed\xe8\xea: \xce\xf4\xe8\xf6\xe8\xe0\xeb\xfc\xed\xfb\xe9'
        }

        self.assertDictEqual(res, true_res)

    def test3(self):
        content = self.get_data('bar-titapet.ru.xml')
        res = BarCi.result(content)

        true_res = {'domain': 'titapet.ru', 'title': '', 'url': '', 'rang': '0', 'value': 0, 'textinfo': ''}
        self.assertDictEqual(res, true_res)

    def test4(self):
        res = BarCi.get_url('http://titapet.ru/')
        self.assertEqual(res, 'http://bar-navig.yandex.ru/u?show=31&url=http://titapet.ru/')

    def test5(self):
        res = BarCi.get_url('titapet.ru')
        self.assertEqual(res, 'http://bar-navig.yandex.ru/u?show=31&url=http://titapet.ru/')

