from scipy.interpolate import *
from math import *

x=[i*1.0 for i in range(1,10)]
y=[1,3,6,10,15,21,28,36,45,55,66,78,91,105,120,136,153,171]

print lagrange(x,y)