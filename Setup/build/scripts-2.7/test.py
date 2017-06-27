import sys
import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print os.path.dirname(os.path.abspath(__file__))
#print path
sys.path.append(path)

import  stuff  

r1 = stuff.razlomak.Razlomak(2,3)
r2 = stuff.razlomak.Razlomak(3,4)
print "2/3 + 3/4 = ", r1+r2
print "2/3 + 3/4 = ", r1*r2


