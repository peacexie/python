#coding=UTF-8

import copy, re, json, random, math
from random import shuffle
from core import argv, dbop, files, urlpy
from urllib import parse, request as ureq
from pyquery import PyQuery as pyq

# 获得字符表
# c : 是否大写
def stab(k='0', c=0):
    tab = {
        '0': '0123456789',
        'a': 'abcdefghijklmnopqrstuvwxyz',
        'b': '3456789abcdfghjkmnpqrstuvwxy',
        'f': 'abcdef',
    }
    r = tab[k]
    if(c):
        r = r.upper()
    return r;

# 随机打乱字符串
def rs(s):
    sl = list(s) # 将字符串转换成列表
    shuffle(sl) # 调用random模块的shuffle函数打乱列表
    return ''.join(sl)

# n个随机字符
# k : 0,a/A,b/B,f/F,
def rn(k, n):
    if not k:
        k = 'b'
    kl = list(k); s0 = re = ''
    chp = ' '
    for ki in kl:
        if ki in '0abf':
            c = 0
        elif ki in 'ABF':
            c = 1; ki = ki.lower()
        else:
            c = 0; ki = 'b'
        s0 += stab(ki, c)
    for i in range(n):
        ch = random.choice(s0) 
        while chp==ch:
            ch = random.choice(s0)
        re += ch
        chp = ch
    return re

# 字符串分组
# rn : 每行rn个
# cm : 每列cm个
def strg(s0, rn, cm, sub=0):
    slen = len(s0); re = {}
    no = 0; ino = 1
    while no<slen:
        istr = s0[no:rn+no]
        re[ino] = istr if sub else strg(istr, cm, 0, 1)
        no += rn
        ino += 1
    return re

def puke(r=1):
    t = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    h = ['♠','♥','♦','♣']
    re = []
    for t0 in t:
        for h0 in h:
            s = h0 +''+ t0
            re.append(s)
    if r:
        random.shuffle(re)
    return re


'''
    define('KEY_NUM10',  '0123456789');
    define('KEY_CHR26',  'abcdefghijklmnopqrstuvwxyz');
    define('KEY_CHR22',  'abcdefghjkmnpqrstuvwxy'); // -iloz
    define('KEY_NUM16',  KEY_NUM10.'abcdef');
    define('KEY_TAB36',  KEY_NUM10.KEY_CHR26); // 极端情况下用
    define('KEY_TAB32',  KEY_NUM10.KEY_CHR22); // (字形可能与数字012混淆)
    define('KEY_TAB30',  '123456789abcdfghjkmnpqrstuvwxy'); // - 0e + iloz (0字形,e读音易混淆)
    define('KEY_TAB24',  '3456789abcdfghjkmnpqrstuvwxy'); // - 012eiloz(25) (去除字形读音易混淆者)
    define('NSP_INIT',   "namespace imcat;\n(!defined('RUN_INIT')) && die('No Init');");
'''
