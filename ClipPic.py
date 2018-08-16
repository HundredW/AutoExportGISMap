#!/usr/bin/env python
# encoding: utf-8
'''
@author: Wanghan
@contact: panda@cug.edu.cn
@software: Pycharm
@file: ClipPic.py
@time: 2018/8/3 11:59
@desc:
'''

from PIL import Image
import matplotlib.pyplot as plt
import os
#PP =u"E:\Export\OutPng300"
PP =u"E:\Export\OutPng2"
PP =u"E:\Export\OutPngDS"
OutPP =u"E:\Export\OutPng300Clip"
imgfiles = os.listdir(PP)
# 72DPI
#box=(0,0,1685,2384)
#box2 =(1685,0,3369,2384)
#box3 =(3369,0,5055,2384)
# 300DPI

box=(0,0,7020,9934)
box2 =(7020,0,14041,9934)
box3 =(14041,0,21062,9934)
for file in  imgfiles:
    name = file.replace('.png','')
    print u"当前处理   "+name
    img=Image.open(PP+"\\"+file)  #打开图像
    print img.size
    roi=img.crop(box)
    roi.save(OutPP+"\\" + name +u"_人口密度图.png")
    roi2=img.crop(box2)
    roi2.save(OutPP + "\\" + name + u"_外籍人口图.png")
    roi3=img.crop(box3)
    roi3.save(OutPP + "\\" + name + u"_外资企业图.png")
print "Done!"
