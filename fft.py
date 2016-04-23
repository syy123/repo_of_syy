# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:19:47 2016

@author: WB
"""

import numpy as np
import pylab as pl
Fs=20
N=256
f1=5
f2=50
#t = np.arange(0,1.0*N/Fs,1.0/Fs)
#t = np.arange(-10.0/rate,10.0/rate,1.0/Fs/rate)
t = np.arange(-10,10,1.0/Fs)
print "len t",len(t)
s = np.cos(2*np.pi*f1*t)+np.sin(2*np.pi*f1*t+np.pi*0.5)
pl.figure()
pl.plot(s)
pl.title(u"原始信号")
pl.grid(True)
pl.figure()
y = np.fft.fft(s,N)
#y = np.fft.fftshift(y)
yf = np.abs(y)
pl.plot(yf)
pl.title(u"fft模值")
pl.grid(True)
pl.figure()
yf1=yf/N
#yf1[0]=yf1[0]
print 'yf1',len(yf1)
f=np.arange(0,Fs,1.0*Fs/N)
print 'f',len(f)
pl.plot(f,yf1)
pl.title(u"幅度-频率")
pl.grid(True)

'''pl.figure()
pyy=np.arange(0,N/2)
for i in range(N/2):
    pyy[i] = np.angle(y[i])
    pyy[i] = pyy[i]*180/np.pi
pl.plot(f[0:N/2],pyy[0:N/2])
pl.title(u"相位-频率")
pl.grid(True)'''
pl.show()
print 'master'

