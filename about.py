#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys
import re

from AppKit import NSWorkspace 

# 获取方法有缺陷,如果是其他脚本间接调用获取到结果是错的
ROOT_PATH = sys.path[0]
DATA_PATH = sys.path[0] + '/data/'

def main():
  op = ''
  if len(sys.argv) > 1:
    op = sys.argv[1]
  else:
    # 没有输入,获取当前程序
    op = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName() 
    pass
  
  filePath = DATA_PATH+op
  if os.path.exists(filePath):
    print os.system("clear")
    print os.system("less "+DATA_PATH+op)
  else:
    print '当前程序:'+op+',没有找到配置' 
    
main()


