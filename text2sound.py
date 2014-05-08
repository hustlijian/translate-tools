#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

URL = 'http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q=' 

def get_url(string):
    if string:
        str_uri = string.replace(' ', '+')
    return URL + str_uri

def text2sound(string):
    '''
    translate string to sound(mp3)
    >>> text2sound('hello world')
    '''
    url = get_url(string)
    r = requests.get(url)
    print r.status_code
    if r.status_code == 200:
        f = open(string.replace(' ', '_')+'.mp3', 'w')
        f.write(r.content)
        f.close()
    else:
        print 'error: %s'%string

def main():
    text2sound('hello world')

if __name__ == '__main__':
    main()
