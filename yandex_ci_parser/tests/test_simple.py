# -*-coding: utf-8 -*-

from yandex_ci_parser.tests import YandexCiParserTests
from yandex_ci_parser.simple import SimpleCi


class SimpleCiTest(YandexCiParserTests):
    def test1(self):
        s = SimpleCi()
        res = s.get_bar('bdbd.ru')
        self.assertEqual(res['value'], 1600)

    def test2(self):
        s = SimpleCi()
        res = s.get_bar('titapet.ru')
        self.assertEqual(res['value'], 0)

    def test3(self):
        s = SimpleCi()
        res = s.get_yaca('titapet.ru')
        self.assertEqual(res, 0)

    def test4(self):
        s = SimpleCi()
        res = s.get_yaca('yandex.ru')
        self.assertEqual(res, 500000)

    def test5(self):
        s = SimpleCi()
        res = s.get_yaca_image('yandex.ru')
        self.assertEqual(res, 500000)

    def test6(self):
        s = SimpleCi()
        res = s.get_yaca_image('apartlux.ru')
        self.assertEqual(res, 150)

    def test7(self):
        s = SimpleCi()
        res = s.get_yaca_image('http://www.ingate.ru/')
        self.assertEqual(res, 1100)


