from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate


nodes = np.array( [ [0, -5], [2, -3.75], [6, -1], [9, 5] ] )

x = nodes[:,0]
y = nodes[:,1]

tck,u     = interpolate.splprep( [x,y] ,s = 0 )
xnew,ynew = interpolate.splev( np.linspace( 0, 1, 100 ), tck,der = 0)

# plt.plot( [0,0],[9,9]. 'k-' )
plt.plot([0, 9], [-5, 5] , 'k-')

plt.plot(  xnew ,ynew )
plt.legend( [ 'Sägezahn' , 'adapt. Sägezahn'] )
plt.axis( [ x.min() - .1 , x.max() + .1 , y.min() - .1 , y.max() + .2 ] )
plt.ylabel("Steuersignal")
plt.xlabel("Zeit")
# plt.plot(  x ,y )

plt.grid()
plt.savefig("SawVsSpline02.eps")