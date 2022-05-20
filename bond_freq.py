#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:12:19 2022

@author: zrollins
"""


#Equilibration
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Arial"
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
#TCR-pMHC H_Number vs Time

t, ha, haa = [], [], []

with open("/Users/zrollins/Documents/Documents/tcrai/tcr0001/afold/num_interface_TCR_pMHC.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 3:
            t.append(float(cols[0]))
            ha.append(float(cols[1]))
            haa.append(float(cols[2]))

t, hb, hbb = [], [], []

with open("/Users/zrollins/Documents/Documents/tcrai/tcr0001/afold/num_interface_CDR3a_pep.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 3:
            t.append(float(cols[0]))
            hb.append(float(cols[1]))
            hbb.append(float(cols[2]))

#TCR-peptide H_Number vs Time

t, hc, hcc = [], [], []

with open("/Users/zrollins/Documents/Documents/tcrai/tcr0001/afold/num_interface_CDR3b_pep.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 3:
            t.append(float(cols[0]))
            hc.append(float(cols[1]))
            hcc.append(float(cols[2]))
            
#PLOT Hbonds vs Time

hbonds = {'Time (ns)': t,'TCR-pMHC':ha,'CDR3\u03B1-CEA':hb, 'CDR3\u03B2-CEA':hc}
df = pd.DataFrame(hbonds)
df2 = pd.DataFrame(hbonds)
df['Time (ns)']=df['Time (ns)'].div(1000)
df['TCR-pMHC']= df.iloc[:,1].rolling(window=500).mean()
df['CDR3\u03B1-CEA']= df.iloc[:,2].rolling(window=500).mean()
df['CDR3\u03B2-CEA']= df.iloc[:,3].rolling(window=500).mean()
ax = plt.gca()
df.plot(kind='line',x='Time (ns)', y='TCR-pMHC', color='lime', ax=ax)
df.plot(kind='line',x='Time (ns)', y='CDR3\u03B1-CEA', ls=':', color= 'green', ax=ax)
df.plot(kind='line',x='Time (ns)', y='CDR3\u03B2-CEA', ls='--', color= 'green', ax=ax)
#df.plot(kind='line',x='Time (ns)', y='TCR-pMHC', color='magenta', ax=ax)
#df.plot(kind='line',x='Time (ns)', y='CDR3\u03B1-CEA', ls=':', color= 'hotpink', ax=ax)
#df.plot(kind='line',x='Time (ns)', y='CDR3\u03B2-CEA', ls='--', color= 'hotpink', ax=ax)
#df.plot(kind='line',x='Time (ns)', y='TCR-pMHC', color='blue', ax=ax)
#df.plot(kind='line',x='Time (ns)', y='CDR3\u03B1-CEA', ls=':', color= 'navy', ax=ax)
#df.plot(kind='line',x='Time (ns)', y='CDR3\u03B2-CEA', ls='--', color= 'navy', ax=ax)
ax.set_ylabel('Number of Hydrogen Bonds', fontsize=20)
ax.set_xlabel('Time (ns)', fontsize=20)
#ax.set_title('H-Bonds vs Time (DMF5_L1 Equilibration)')
ax.set_ylim(0,20)
plt.savefig('/Users/zrollins/Documents/Documents/tcrai/tcr0001/afold/hbonds_t_eq.png', bbox_inches='tight',dpi=300)
plt.show()


#Partition H-Bonds & Time
max_t=(t[-1]-t[0])/10
h_max = max(ha)
hndx = np.arange(0,h_max+2,1)
hndx = hndx.tolist()

df3 = df2.groupby('TCR-pMHC')['Time (ns)'].size().reindex(hndx)
df3.fillna(0, inplace=True)
df3= df3.to_frame()
df3['H-Bond Frequency (TCR-pMHC)']= df3['Time (ns)']/max_t
df3.to_excel('/Users/zrollins/Documents/Documents/tcrai/tcr0001/afold/hfrequency.xlsx')
print(df3)





