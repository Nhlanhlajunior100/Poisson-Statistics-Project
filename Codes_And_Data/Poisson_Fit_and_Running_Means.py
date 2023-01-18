# -*- coding: utf-8 -*-
"""
Created on Sun May 23 04:49:21 2021

@author: Nhlanhla Hlengane
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
mu=4
g=np.genfromtxt('Background.txt')
h=np.genfromtxt('mu4.txt')


xdata=h
    
#Arithmetic mean
N=0   
sumx=0 
for i in xdata:    
    sumx=sumx+i
    N+=1
xbar=(1/N)*sumx
print("arithmetic mean is:",xbar)
print("arithmetic mean uncertaiinty is:",(np.sqrt(xbar/N)))


#Sample variance
sumxmxbar=0
for i in xdata:
    xmxbar=(i-xbar)**2
    sumxmxbar+=xmxbar
    
Ssquared = (1/(N-1))*sumxmxbar
print("Sample Variance is:",Ssquared)




v=((2*100*(np.mean(xdata)**2)+(100-1)*np.mean(xdata))/(100*(100-1)))**(1/2)

print("Sample variance uncertainty is:",v)
J=[]
r=[]
yerror=[]

#The running mean
for j in range(1, 101):
        x = 0
        J.append(j)                                      #sequence no. of the interval count
        for i in range(100):
            x += xdata[i] 
            if (i+1)==j:
                r.append((1/j)*x)                        #running mean
                yerror.append((r[i]/j)**(1/2))        #uncertainty
            if i>j:
                break

    
plt.errorbar(J, r, yerr=yerror,fmt='.', marker='s', ms=3, ecolor='k', mfc='red', mec='red', elinewidth=1, capsize=2, capthick=1, label='Running mean')
plt.title("Background")
plt.xlabel("Sequence number")
plt.ylabel("Cumulative mean")
plt.grid()
plt.show()


k=0
bins=[]
binwidth=[]
l=0
binlen=1.5
binnumber=[]
cpt=[]
i=0
n=0
counts_per_trial=[]
while l<=200:
    counts_per_trial.append(l)
    cpt.append(l)
    l+=binlen

D = len(cpt)
  

count=0
countlist=[]
y=[]
yerror=[]
checklist=[]
k=0
interval=[]

#Creating number of trials with this number of counts
for i in range(len(cpt)):
    for k in xdata:
        if cpt[i]<k and k<=cpt[i+1]:
            count+=1
    y.append(count)
    count=0



#poisson equation      

domain=150
pts=150
xtrue =np.linspace(0,domain,pts)
ytrue = np.zeros(pts)
for i in range(domain):
        ytrue[i]=100*binlen*(((mu**xtrue[i])/gamma(xtrue[i]+1))*np.e**(-mu))
check=0

#changing initial value of y
for i in range(len(y)):
    #Changing initial value
    if i>0:
        if y[i-1]<=5:
            y[i]+=y[i-1]
            y[i-1]=0
    if y[i]>5:
        break
#changing the final value  of y
for j in range(len(y)):
    if y[len(y)-(j+1)]<=5:
        y[len(y)-(j+2)]+=y[len(y)-(j+1)]
        y[len(y)-(j+1)]=0
    if y[len(y)-(j+2)]>5:
        break
    
for i in range(len(y)):
    yerror.append(np.sqrt(y[i]*(1-y[i]/100)))

plt.plot(xtrue,ytrue, label="Poisson curve")
plt.errorbar(cpt, y, yerr=yerror,fmt='.', marker='s', ms=3, ecolor='k', mfc='red', mec='red', elinewidth=1, capsize=2, capthick=1, label='Binned data')
plt.xlim(0,30)
plt.ylim(0.2)
plt.ylabel("Number of trials with \nthis number of counts")
plt.title("Background")
plt.xlabel("Counts per trial")
plt.legend()
plt.grid()
plt.show()

  
    