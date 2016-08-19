# coding=utf-8



import json
import codecs
import os
import sys

if __name__ == '__main__':

    fr = codecs.open(sys.argv[1], 'r', encoding='utf-8')
    fw = codecs.open(sys.argv[2], 'w', encoding='utf-8')

    a = fr.read()
    obj = json.loads(a)
    RECORDS = obj.get('RECORDS')
    allcouont = 0
    okcount = 0
    for i in RECORDS:
        allcouont += 1
        try:
            st = json.dumps(i, ensure_ascii=False)
            fw.write(st)
            fw.write(os.linesep)
            okcount += 1

        except Exception as e:
            print str(e)

    pass
