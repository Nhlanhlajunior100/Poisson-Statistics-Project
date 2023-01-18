# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:22:52 2021

@author: Kryptic Nessi
"""
import matplotlib.pyplot as plt
import numpy as np
#SampleVariance
mu30SV=27.26575757575758
mu100SV=132.08838383838386
mu10SV= 8.259696969696972
mu4SV=6.773636363636366
BKGSV= 3.638282828282831

#Arithmetic mean
mu30AM=31.13
mu100AM=102.75
mu10AM=10.27
mu4AM=6.29
BKGAM=4.91


Ss=[BKGSV/BKGAM,mu4SV/mu4AM,mu10SV/mu10AM,mu30SV/mu30AM,mu100SV/mu100AM]
Ss_u=[0.732210573013203,0.9285336544653336,1.4944783894609037,4.459664910182278,14.63]
xb=[BKGAM,mu4AM,mu10AM,mu30AM,mu100AM]
xb_u=[0.2215851980616034,0.25079872407968906,0.3204684071792413,0.5579426493825328,1.0136567466356647]


yerror = []
for i in range(5):
    yerror.append((Ss[i]/xb[i])*(np.sqrt((Ss_u[i]/Ss[i])**2+(xb_u[i]/xb[i])**2)))




plt.errorbar(xb, Ss, yerr=yerror,fmt='.', marker='s', ms=3, ecolor='k', mfc='red', mec='red', elinewidth=1, capsize=2, capthick=1, label='unkownyet')
plt.ylim(0,2)
plt.grid()
plt.title("Sample variance to arithmetic mean ratio")
plt.ylabel("Sample variance/Arithmatic mean")
plt.xlabel("Arithmetic mean")
plt.show()
print(yerror) #confirm these using a calculator
#plt.scatter(xbararr,Ssquared_xbar)

#fraction of bins that agree with the poisson plot within one standard deviation
mu=[4,10,30,100]
bin_frac=[4/7,4/7,5/8,7/9]
Nbins=[7,7,8,9]
u_bins=[]
#fraction uncertainty
for i in range(4):
    u_bins.append(np.sqrt(bin_frac[i]*(1-(bin_frac[i])/Nbins[i])))

plt.errorbar(mu, bin_frac, yerr=u_bins,fmt='.', marker='s', ms=3, ecolor='k', mfc='red', mec='red', elinewidth=1, capsize=2, capthick=1, label='unkownyet')
#plt.ylim(0,3)
plt.title("Fraction of bins described by the Poisson distribution \nas a function of the mean rate")
plt.xlabel("mean rate")
plt.ylabel("Fraction of bins that are described \nby the Poisson distribution")                                      
plt.grid()

