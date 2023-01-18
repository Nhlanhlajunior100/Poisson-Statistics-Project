# -*- coding: utf-8 -*-
"""
Created on Fri May 21 17:10:35 2021

@author: Trancrypt
"""

import numpy as np
import matplotlib.pyplot as plt

mu100 = np.genfromtxt('1642965_mu100.txt')
data4 = np.genfromtxt('mu4.txt')
data10 = np.genfromtxt('mu10.txt')
data30 = np.genfromtxt('mu30.txt')
data100 = np.genfromtxt('mu100.txt')
dataBKG = np.genfromtxt('1642965_BKG.txt')

data = [data4, data10, data30, data100,mu100, dataBKG]

N = len(data4)
r = [[],[],[],[],[]]
J = [[],[],[],[],[]]
yerror = [[],[],[],[],[]]
 
for k in range(5):
    for j in range(1, N+1):
        x = 0
        J[k].append(j)                                      #sequence no. of the interval count
        for i in range(N):
            x += data[k][i] 
            if (i+1)==j:
                r[k].append((1/j)*x)                        #running mean
                yerror[k].append((r[k][i]/j)**(1/2))        #uncertainty
            if i>j:
                break
    #plt.errorbar(J[k], r[k], yerr=yerror[k], fmt = '.', marker = 's', mfc = 'red', mec = 'red', ms = 3, mew = 1, ecolor = 'black', elinewidth = 1, capsize=2, capthick = 1, label = 'something')
    #plt.show()

############################################################################################################################################
#S^2 Measurement
                
xbar = []
s_sq = []
xbar_err = []
s_sq_err = []
sox = []
for l in range(5):
    xbar.append(0)
    s_sq.append(0)
    for m in range(N):
        xbar[l] += (1/100)*data[l][m]                       #xbar sum
    xbar_err.append((xbar[l]/N)**(1/2))                     #delta xbar
    for o in range(N):
        s_sq[l] += ((data[l][o]-xbar[l])**2)/(N-1)          #s_squared sum
    s_sq_err.append(((2*N*(xbar[l]**2)+(N-1)*xbar[l])/(N*(N-1)))**(1/2)) #delta s_squared
    sox.append(s_sq[l]/xbar[l])


print("arithmetic mean: ")
print(xbar)
print("arithmetic mean uncertainties: ")
print(xbar_err)
print("Variance: ")
print(s_sq)
print("Variance uncertainties: ")
print(s_sq_err)
print("S squared over arithmetic mean:")
print(sox)


















