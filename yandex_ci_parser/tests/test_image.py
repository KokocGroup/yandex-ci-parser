# -*-coding: utf-8 -*-

from yandex_ci_parser.tests import YandexCiParserTests
from yandex_ci_parser.image import ImageCi


class ImageCiTest(YandexCiParserTests):
    def test1(self):
        content = self.get_data('ci-apartlux.ru.gif')
        res = ImageCi.result(content)
        self.assertEqual(res, 150)

    def test2(self):
        content = self.get_data('ci-bdbd.ru.gif')
        res = ImageCi.result(content)
        self.assertEqual(res, 1600)

    def test3(self):
        content = self.get_data('ci-titapet.ru.gif')
        res = ImageCi.result(content)
        self.assertEqual(res, None)

    def test4(self):
        content = self.get_data('ci-yandex.ru.gif')
        res = ImageCi.result(content)
        self.assertEqual(res, 500000)
