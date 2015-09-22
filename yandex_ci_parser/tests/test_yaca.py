# -*-coding: utf-8 -*-

from yandex_ci_parser.tests import YandexCiParserTests
from yandex_ci_parser.yaca import YacaCi
from yandex_ci_parser.errors import IncorrectParserError


class YacaCiTest(YandexCiParserTests):
    def test1(self):
        content = self.get_data('yaca-bdbd.ru.html')
        res = YacaCi.result(content, 'bdbd.ru')
        self.assertEqual(res, 1600)

    def test2(self):
        content = self.get_data('yaca-bdbd.ru.html')
        res = YacaCi.result(content, 'http://bdbd.ru')
        self.assertEqual(res, 1600)

    def test3(self):
        content = self.get_data('yaca-yandex.ru.html')
        res = YacaCi.result(content, 'http://yandex.ru')
        self.assertEqual(res, 500 * 1000)

    def test4(self):
        content = self.get_data('yaca-yandex.ru.html')
        res = YacaCi.result(content, 'yandex.ru')
        self.assertEqual(res, 500 * 1000)

    def test5(self):
        content = self.get_data('yaca-titapet.ru.html')
        res = YacaCi.result(content.decode('utf8'), 'titapet.ru')
        self.assertEqual(res, 0)

    def test6(self):
        content = self.get_data('yaca-titapet.ru.html')
        res = YacaCi.result(content.decode('utf8'), 'http://titapet.ru')
        self.assertEqual(res, 0)

    def test7(self):
        content = self.get_data('yaca-y0u-money.ru.html')
        res = YacaCi.result(content.decode('utf8'), 'http://y0u-money.ru')
        self.assertEqual(res, None)

    def test8(self):
        content = self.get_data('yaca-y0u-money.ru.html')
        res = YacaCi.result(content.decode('utf8'), 'y0u-money.ru')
        self.assertEqual(res, None)

    def test9(self):
        res = YacaCi.get_url('y0u-money.ru')
        self.assertEqual(res, 'http://yaca.yandex.ru/yca/cy/ch/y0u-money.ru/')

    def test10(self):
        content = self.get_data('yaca-apartlux.ru.html')
        with self.assertRaises(IncorrectParserError):
            res = YacaCi.result(content.decode('utf8'), 'apartlux.ru')
