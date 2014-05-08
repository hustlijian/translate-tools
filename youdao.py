#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib
import requests
import json

VERSION = 1.1
URL = 'http://fanyi.youdao.com/openapi.do?'
KEY_FROM = 'hustlijian-cnblog'
KEY = '16418109'
TYPE = 'data'
DOC_TYPE = 'json'


def translate(string):
    uri_dict = {}
    uri_dict['version'] = VERSION
    uri_dict['keyfrom'] = KEY_FROM
    uri_dict['key'] = KEY
    uri_dict['type'] = TYPE
    uri_dict['doctype'] = DOC_TYPE
    uri_dict['q'] = string
    uri = urllib.urlencode(uri_dict)
    #print uri
    url = URL + uri
    #print url
    response = requests.get(url)
    return json.loads(response.content)

def show(data):
    #print data
    #res = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
    #print res
    print '\n基本信息'
    print '-'*10
    print 'you query: %s'%data['query']
    print 'return code: %d'%data['errorCode']
    print 'translation: %s'%','.join(data['translation'])
    print '\n基本词典'
    print '-'*10
    basic = data['basic']
    print 'phonetic: %s'% basic['phonetic']
    print 'uk: %s'% basic['uk-phonetic']
    print 'us: %s'% basic['us-phonetic']
    print 'explains: %s'% ',\n'.join(basic['explains'])
    print '\n网络释义'
    print '-'*10
    web = data['web']
    for item in web:
        print 'key: %s'%item['key']
        print 'value: %s'%', '.join(item['value'])



def main():
    if sys.argv and len(sys.argv) >= 2:
        l = ' '.join(sys.argv[1:])
        #print l
        data = translate(l)
        show(data)
    else:
        print '有道翻译： \n\t提示：请输入您要翻译的词或句子'


if __name__ == '__main__':
    main()
