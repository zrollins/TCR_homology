#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:43:12 2022

@author: zrollins
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Arial"
plt.rc('xtick',labelsize=15)
plt.rc('ytick',labelsize=15)

t, c = [], []
with open("/Users/zrollins/Documents/Documents/tcrai/tcr0001/modeller/clust-id_alleq.xvg") as f:
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

clust = {'Time (ns)': t,'Cluster':c}
df = pd.DataFrame(clust)
df_5= df[df['Cluster']<=10]
df_5['Time (ns)']=df_5['Time (ns)'].div(1000)
print(df_5)
ax = plt.gca()
ax.set_ylabel('Cluster Number',fontsize=20)
ax.set_xlabel('Time (ns)',fontsize=20)
df_5.plot(kind='scatter',x='Time (ns)', y='Cluster', color='lime', fontsize=20, marker="|",s=100, ax=ax)
plt.savefig('/Users/zrollins/Documents/Documents/tcrai/tcr0001/modeller/clusters_all.png', bbox_inches='tight',dpi=300)
plt.show()


t, c = [], []
with open("/Users/zrollins/Documents/Documents/tcrai/tcr0002/modeller/clust-id_alleq.xvg") as f:
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

clust = {'Time (ns)': t,'Cluster':c}
df = pd.DataFrame(clust)
df_5= df[df['Cluster']<=10]
df_5['Time (ns)']=df_5['Time (ns)'].div(1000)
ax = plt.gca()
ax.set_ylabel('Cluster Number',fontsize=20)
ax.set_xlabel('Time (ns)',fontsize=20)
df_5.plot(kind='scatter',x='Time (ns)', y='Cluster', color='magenta', fontsize=20, marker="|",s=100,ax=ax)
plt.savefig('/Users/zrollins/Documents/Documents/tcrai/tcr0002/modeller/clusters_all.png', bbox_inches='tight',dpi=300)
plt.show()

t, c = [], []
with open("/Users/zrollins/Documents/Documents/tcrai/tcr0003/modeller/clust-id_alleq.xvg") as f:
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

clust = {'Time (ns)': t,'Cluster':c}
df = pd.DataFrame(clust)
df_5= df[df['Cluster']<=10]
df_5['Time (ns)']=df_5['Time (ns)'].div(1000)
ax = plt.gca()
ax.set_ylabel('Cluster Number',fontsize=20)
ax.set_xlabel('Time (ns)',fontsize=20)
df_5.plot(kind='scatter',x='Time (ns)', y='Cluster', color='blue', fontsize=20, marker="|",s=100,ax=ax)
plt.savefig('/Users/zrollins/Documents/Documents/tcrai/tcr0003/modeller/clusters_all.png', bbox_inches='tight',dpi=300)
plt.show()