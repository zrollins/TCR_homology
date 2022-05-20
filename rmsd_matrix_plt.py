#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:47:09 2022

@author: zrollins
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/zrollins/Documents/Documents/tcrai/TCR1_rmsd', delimiter='\s+', skiprows=1, header=None, index_col=0)
ndx = df.index.tolist()

df.set_axis(ndx, axis=1, inplace=True)
df=df/10
df=df.round(decimals=2)
min_val = min(df)
max_val = max(df)

fig, ax = plt.subplots()
plt.rcParams["figure.figsize"] = [15, 7]
plt.rcParams["figure.autolayout"] = True
plt.rcParams["font.family"] = "Arial"
plt.rc('xtick',labelsize=15)
plt.rc('ytick',labelsize=15)
pos = ax.matshow(df, cmap='RdYlBu_r')

for i in range(len(df)):
   for j in range(len(df)):
      c = df.iloc[i,j]
      ax.text(i, j, str(c), va='center', ha='center',fontsize=12)
      
fig.colorbar(pos,ax=ax)
##TCR1
TCR1_lbls = ['M-C1-250ns', 'M-C1-299ns','M-C2-250ns','M-C2-299ns','M-C7-250ns','M-C7-299ns',
         'C-C1-100ns', 'C-C1-150ns','C-C2-109ns','C-C2-50ns','C-C4-25ns','C-C4-60ns']
##TCR2
TCR2_lbls = ['M-C1-138ns', 'M-C1-200ns','M-C9-128ns','M-C9-138ns','M-C12-150ns','M-C12-196ns',
         'C-C1-100ns', 'C-C1-150ns','C-C3-100ns','C-C3-150ns','C-C4-126ns','C-C4-63ns']
##TCR3
TCR3_lbls = ['M-C1-150ns', 'M-C1-199ns','M-C6-150ns','M-C6-158ns','M-C9-180ns','M-C9-200ns',
         'C-C1-150ns', 'C-C1-200ns','C-C3-150ns','C-C3-199ns','C-C6-150ns','C-C6-200ns']

ax.tick_params(axis="x", bottom=True, top=False, labelbottom=True, labeltop=False)
plt.yticks(ticks=range(0,12,1),labels=TCR1_lbls)
plt.xticks(ticks=range(0,12,1),labels=TCR1_lbls)
plt.setp([tick.label1 for tick in ax.xaxis.get_major_ticks()], rotation=45,
         ha="right", va="center", rotation_mode="anchor")

plt.savefig('/Users/zrollins/Documents/Documents/tcrai/RMSD_TCR1.png', bbox_inches='tight', dpi=300)