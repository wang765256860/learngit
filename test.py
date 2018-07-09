#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-05 17:22:12
# @Author  : WangZhen (wang765256860@gmail.com)
# @Link    : come soon
# @Version : $Id$

try:
	print('try...')
	r = 10/0
	print('result:',r)
except Exception as e:
	print('except',e)
finally:
	print('finally')
