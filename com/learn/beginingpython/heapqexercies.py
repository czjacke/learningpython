#!/usr/bin/python
# -*- coding: UTF-8 -*-
from heapq import *
from random import shuffle
data = list(range(1,10))
print(type(data))

print(data)
#
shuffle(data)
print(data)
heap = []
for n in data:
	heappush(heap, n)
print(heap)

heappush(heap, 0.5)

print(heap)


import shelve
s = shelve.open('../tmp/test.dat',writeback=True                                                                  )
s['x'] = ['a','b','c']
s['x'].append('d')
print(s['x'])