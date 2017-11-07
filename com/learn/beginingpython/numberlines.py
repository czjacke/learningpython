#!/usr/bin/python                                      # 1
# -*- coding: UTF-8 -*-                                # 2
import fileinput                                       # 1# 1# 1# 3
                                                       # 2# 2# 2# 4
for line in fileinput.input(inplace=True):             # 3# 3# 3# 5
	line = line.rstrip()                                  # 4# 4# 4# 6
	num  =  fileinput.lineno()                            # 5# 5# 5# 7
	print('%-55s#%2i'% (line, num))                       # 6# 6# 6# 8
