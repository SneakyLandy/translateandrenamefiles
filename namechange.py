# -*- coding: utf-8 -*-

import os
import string
from translation import baidu, youdao, iciba
import re

regex = re.compile('[%s]' % re.escape(string.punctuation))
for filename in os.listdir(u"C:\\Users\\Andy\\Desktop\\project\\download\\"):
    name, extension = os.path.splitext(filename)
    temp = name.split(" - ")
    print temp
    if '\u' in repr(temp[1]):
        #print filename
        newname = ''
        newname =  youdao(temp[1], dst='en')
        #if name != newname:
        newname = regex.sub('', newname)
        #print newname

        #print "南瓜"
        #newfilename =''.join(c for c in filename if c in string.printable)
        if all(ord(c) < 128 for c in newname):
            os.rename(os.path.join(u'C:\\Users\\Andy\\Desktop\\project\\download\\', filename), os.path.join(u'C:\\Users\\Andy\\Desktop\\project\\download\\', name + ' '+newname + extension))
    #print extension
    #print '哈哈'.decode('utf-8').split()

#print youdao('南瓜',dst='en')
