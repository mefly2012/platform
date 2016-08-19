# -*- coding: utf-8 -*-






import codecs
import requests
import json

if __name__ == '__main__':

    with codecs.open('url_and_tables.txt', 'r', encoding=u'utf-8') as fl:
        for line in fl:
            if not line.strip():
                break
            url, table = line.strip().split()
            a = requests.get(url)
            f2 = codecs.open(table + '_format.txt', 'w', encoding='utf-8')
            f2.write(json.dumps(a.json(), ensure_ascii=False))
            f2.close()
