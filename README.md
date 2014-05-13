translate-tools
===============

Tools to Implement a small en-cn dictionary

description
---------------

1. text2sound.py: use google translate API to change string into mp3 format sound;  
2. youdao.pp: use youdao translate API to get detail translate information;  
3. words.txt: file comtain 264061 word.  

example
---------------
1.  get hello_word.mp3:   

```
(! 118)->ls
LICENSE  README.md  text2sound.py  words.txt  youdao.py
(! 119)->python text2sound.py 
200
(! 120)->ls
hello_world.mp3  LICENSE  README.md  text2sound.py  words.txt  youdao.py

```

2. get chinese information of 'hello':  

```
(! 122)->python youdao.py hello

基本信息
----------
you query: hello
return code: 0
translation: 你好

基本词典
----------
phonetic: hə'ləʊ; he-
uk: hə'ləʊ; he-
us: hɛˈlo, hə-
explains: n. 表示问候， 惊奇或唤起注意时的用语,
int. 喂；哈罗,
n. (Hello)人名；(法)埃洛

网络释义
----------
key: Hello
value: 哈啰, 哈啰你好, 霍经伦
key: Hello Kitty
value: 昵称, 凯帝猫, 匿称
key: Hello Fred
value: 你好
```

REF
------------
1. youdao API, [link](http://fanyi.youdao.com/openapi?path=data-mode)
2. google translate API, [link](http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q=hello)
