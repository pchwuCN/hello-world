#!/usr/bin/python

g = lambda x:x+1
foo = {1,3,5,7,8,9}

print reduce(lambda x,y: (x+y)+(x-y), foo)
