#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 12:47:24 2022

@author: zrollins
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pymbar import timeseries

plt.rcParams["font.family"] = "Times New Roman"
plt.rc('xtick',labelsize=15)
plt.rc('ytick',labelsize=15)

t, a = [], []
with open("/Users/zrollins/Documents/Documents/tcrai/tcr0001/afold/RMSD.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 2:
            t.append(float(cols[0]))
            a.append(float(cols[1]))

t=t[:15000]   
a=a[:15000]           
a = np.array(a)
[t0, g, Neff_max] = timeseries.detectEquilibration(a)
a_equlibrated = a[t0:]
eqt_a = (len(t)-len(a_equlibrated))*10

t, b = [], []
with open("/Users/zrollins/Documents/Documents/tcrai/tcr0002/afold/RMSD.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 2:
            t.append(float(cols[0]))
            b.append(float(cols[1]))
              
b = np.array(b)
[t0, g, Neff_max] = timeseries.detectEquilibration(b)
b_equlibrated = b[t0:]
eqt_b = (len(t)-len(b_equlibrated))*10    

t, c = [], []
with open("/Users/zrollins/Documents/Documents/tcrai/tcr0003/afold/RMSD.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 2:
            t.append(float(cols[0]))
            c.append(float(cols[1]))
            
c = np.array(c)
[t0, g, Neff_max] = timeseries.detectEquilibration(c)
c_equlibrated = c[t0:]
eqt_c = (len(t)-len(c_equlibrated))*10   

t, d = [], []
with open("/Users/zrollins/Documents/Documents/tcrai/tcr0001/modeller/RMSD.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 2:
            t.append(float(cols[0]))
            d.append(float(cols[1]))
#t=t[:12500]   
#d=d[:12500]  
            
d = np.array(d)
[t0, g, Neff_max] = timeseries.detectEquilibration(d)
d_equlibrated = d[t0:]
eqt_d = (len(t)-len(d_equlibrated))*10   

t, e = [], []
with open("/Users/zrollins/Documents/Documents/tcrai/tcr0002/modeller/RMSD.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 2:
            t.append(float(cols[0]))
            e.append(float(cols[1]))
        
e = np.array(e)
[t0, g, Neff_max] = timeseries.detectEquilibration(e)
e_equlibrated = e[t0:]
eqt_e = (len(t)-len(e_equlibrated))*10

t, h = [], []
with open("/Users/zrollins/Documents/Documents/tcrai/tcr0003/modeller/RMSD.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 2:
            t.append(float(cols[0]))
            h.append(float(cols[1]))
            
h = np.array(h)
[t0, g, Neff_max] = timeseries.detectEquilibration(h)
h_equlibrated = h[t0:]
eqt_h = (len(t)-len(h_equlibrated))*10      
            
tcr = {'TCR1a':eqt_a,'TCR2a':eqt_b,'TCR3a':eqt_c, 'TCR1m':eqt_d,'TCR2m':eqt_e,'TCR3m':eqt_h}
df = pd.DataFrame([tcr])
#df.to_csv('/Users/zrollins/Documents/Documents/tcrai/tcr0003/afold/eqt_tcr3_afold.csv')
print(df)


