#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys
import re

from AppKit import NSWorkspace 

# 获取方法有缺陷,如果是其他脚本间接调用获取到结果是错的
ROOT_PATH = sys.path[0]
DATA_PATH = sys.path[0] + '/data/'

def opApp(filePath, op):
  if op == '':
    print os.system("clear")
    print os.system("less "+filePath)
  elif op == '-edit':
    os.system("vim "+filePath)
  else:
    pass

def main():
  app = ''
  if len(sys.argv) > 1:
    app = sys.argv[1]
  else:
    # 没有输入,获取当前程序
    app = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName() 
    pass

  op = '' 
  if len(sys.argv) > 2:
    op = sys.argv[2]

  filePath = DATA_PATH + app
  if os.path.exists(filePath):
    opApp(filePath, op)
  else:
    print '当前程序:'+app+',没有找到配置' 

    
main()
