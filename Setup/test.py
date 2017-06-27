import sys
import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print os.path.dirname(os.path.abspath(__file__))
#print path
sys.path.append(path)

import  Stuff.stuff 

r = stuff.Razlomak(1,2)
print r
