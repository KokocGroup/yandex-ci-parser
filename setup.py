from setuptools import setup


VERSION = "0.0.2"

setup(
    name='yandex-ci-parser',
    description="Fetch yandex ci",
    version=VERSION,
    url='https://github.com/KokocGroup/yandex-ci-parser',
    download_url='https://github.com/KokocGroup/yandex-ci-parser/tarball/v{0}'.format(VERSION),
    packages=['yandex_ci_parser'],
    install_requires=[],
)
