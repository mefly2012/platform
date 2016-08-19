# -*- coding: utf-8 -*-

import  requests






if __name__=='__main__':
    url = 'http://www.baidu.com'

    a=requests.get(url)
    # print a.content
    print a.status_code
    pass