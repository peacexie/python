#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
一般来说，第三方库都会在Python官方的pypi.python.org网站注册，
要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，
比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
easy_install.exe Pillow
"""

from PIL import Image
im = Image.open('mod_vcode.jpg')
print(im.format, im.size, im.mode)
#PNG (400, 300) RGB
im.thumbnail((60, 30))
im.save('mod_3rd-thumb.jpg', 'JPEG')