# yandex-ci-parser
Yandex ci parser. See detail https://yandex.ru/support/catalogue/citation-index/tic-about.xml

## Usage

###Fetch bar ci
```
import requests
from yandex_ci_parser.bar import BarCi

site = 'http://yandex.ru'
url = BarCi.get_url(site)
res = requests.get(url)
res.raise_for_status()
print BarCi.result(res.text)
```

### Fetch yaca ci
```
import requests
from yandex_ci_parser.yaca import YacaCi

site = 'http://yandex.ru'
url = YacaCi.get_url(site)
res = requests.get(url)
res.raise_for_status()
print YacaCi.result(res.text, site)
```

### Fetch yaca ci from image
```
import requests
from yandex_ci_parser.image import ImageCi

url = ImageCi.get_url(site)
res = requests.get(url)
res.raise_for_status()
print ImageCi.result(res.content)
```

