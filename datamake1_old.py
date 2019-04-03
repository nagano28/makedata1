# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 19:20:19 2017

@author: Nagano Masatoshi
"""

import numpy as np
import matplotlib.pyplot as plt

data = []

def makedata():      
    i = 0
    e = 0 
    z = 13
    while i < z:
        a = [0,2,4,6,8]
        j = np.random.randint(0,5)
        b = np.random.randint(10,15)
        e += b
        while b > 0:
             c = a[j] + np.random.normal(0,0.3)
             data.append(c)
             b = b-1
        i=i+1

    np.savetxt('data_old.txt',data)
    #all_data = np.concatenate( data, 0 )

def normalize():
    means = np.mean( data, 0 )
    maxvars = np.max( data-means, 0 )
    new_data = []
    
    #plt
    timelen = range(len(data))
    plt.plot(timelen,data)
    plt.show()
    
    #normalize
    for i in range(len(data)):
        data[i] = (data[i]-means)/maxvars
        #print data[0]
        new_data.append(data[i]) 
    np.savetxt('data_old_norma.txt',new_data) #save
    
    #plot
    timelen = range(len(new_data))
    plt.plot(timelen,new_data)
    plt.show()


def main():
    makedata()
    normalize()



if __name__ == '__main__':
    main()