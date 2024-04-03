import numpy as np
from numpy import random
'''
for i in range(6):
    print(random.randint(6))

for i in range(6):
    print(random.rand(6))

a = random.randint(100,size=(3,5))
print(a)

f = random.rand(3,5)

ch = [ 22, 55, 77, 99, 12, 5, 98, 42]
print(random.choice(ch,size=(2,3)))

print(random.choice(ch, p=[0.1, 0.25, 0.1, 
                           0.09, 0.35, 0.05, 
                           0.05, 0.01],size=10))
# '''

# '''
import os 

fname="qi_randomdata.csv"

if (os.path.isfile(fname)):
    qi = np.loadtxt(fname)
else:
    i_mean = int(input("Mean:"))
    i_std = int(input("Standard Deviation:"))
    i_size = int(input("How many samples:"))

    qi = random.normal(size=i_size, loc=i_mean,scale=i_std)
    np.savetxt(fname,qi)

import matplotlib.pyplot as plt 
# pip install matplotlib
# conda install -c conda-force matplolib

'''
x = np.linspace(0,2*np.pi,200)
y= np.sin(x)
y1= np.cos(x)

plt.subplot(1,2,1)
plt.axhline(0,color='red')
plt.plot(x,y)
plt.plot(x,y1,color='green')
plt.subplot(1,2,2)
plt.plot(x,y1,color='green')
plt.axhline(0,color='red') 

plt.show()
# '''


# TODO: draw mean, 1*std(70%) and 2*std (95%) lines opt 3*std  (99%)
mean=100
std=15

len=15
x=np.arange(len)
plt.subplot(1,2,1)
# plt.plot(x,qi[:len],"x")
plt.bar(x,qi[:len])
plt.xlabel("id")
plt.ylabel("QI")
plt.title(("QI Bars"))

plt.axhline(mean,color="red")
plt.axhline(mean+std,color="orange")
plt.axhline(mean-std,color="orange")
plt.axhline(mean+2*std,color="yellow")
plt.axhline(mean-2*std,color="yellow")

#
plt.subplot(1,2,2)
plt.plot(x,qi[:len],"+", linestyle="dotted")
plt.xlabel("id")
plt.ylabel("QI")
plt.title(("QI Dots"))

plt.axhline(mean,color="red")
plt.axhline(mean+std,color="orange")
plt.axhline(mean-std,color="orange")
plt.axhline(mean+2*std,color="yellow")
plt.axhline(mean-2*std,color="yellow")


plt.show()
