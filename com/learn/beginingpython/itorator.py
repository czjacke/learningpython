#!/usr/bin/python
# -*- coding: UTF-8 -*

nest = [[1,2],[3,4],[5]]

#生成器
def flatten(nested):
	for sublist in nested:
		for element in sublist:
			yield element

for num in flatten(nest):
	print(num)

x = sum(i**2 for i in range(2))
print("迭代")
print(x)