#!/usr/bin/env python
'''
	Example of how to use the module
'''

objectRS = RSanalysis()
file = open("input.txt", "r") 
timeSeries = list(map(float, file.read().split(",")))
print(objectRS.run(timeSeries))