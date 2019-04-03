
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 19:20:19 2017

@author: Nagano Masatoshi
"""
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt

#data作成
x_v = 0.4 #x分散
y_v = 0.4 #y分散
classes = ((0,11,x_v,y_v),(2,12,x_v,y_v),(4,10,x_v,y_v),(6,11,x_v,y_v),(8,11,x_v,y_v))
c = classes
data = []
time=[]
for i in range(14):
    a = np.random.randint(0,5)   
    for j in range(int(np.random.normal(c[a][1],c[a][2]))):
        data.append(np.random.normal(c[a][0],c[a][3]))
        time.append(j)

timelen = range(len(data))
plt.plot(timelen,data)
plt.show()


#保存正規化前
np.savetxt('data.txt',data)



#正規化
means = np.mean( data, 0 )
maxvars = np.max( data-means, 0 )
newdata = []
for i in range(len(data)):
    data[i] = (data[i]-means)/maxvars
    newdata.append(data[i]) 

timelen = range(len(newdata))
plt.plot(timelen,newdata)
plt.show()

#保存正規化後
np.savetxt('data_norma.txt',newdata)