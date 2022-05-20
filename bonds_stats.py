#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 08:48:58 2022

@author: zrollins
"""


#Equilibration
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import scipy.stats as stats
import matplotlib.pyplot as plt
from pingouin import pairwise_tukey
from openpyxl import load_workbook

"""
path=r'/Users/zrollins/Documents/Documents/tcrai/bonds_stats.xlsx'
book = load_workbook(path)
writer=pd.ExcelWriter(path, engine = 'openpyxl')
writer.book=book"""


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

t1, hb, hbb = [], [], []

with open("/Users/zrollins/Documents/Documents/tcrai/tcr0001/modeller/num_interface_TCR_pMHC.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 3:
            t1.append(float(cols[0]))
            hb.append(float(cols[1]))
            hbb.append(float(cols[2]))
            
t, hc, hcc = [], [], []

with open("/Users/zrollins/Documents/Documents/tcrai/tcr0002/afold/num_interface_TCR_pMHC.xvg") as f:
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

t1, hd, hdd = [], [], []

with open("/Users/zrollins/Documents/Documents/tcrai/tcr0002/modeller/num_interface_TCR_pMHC.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 3:
            t1.append(float(cols[0]))
            hd.append(float(cols[1]))
            hdd.append(float(cols[2]))
            
t, he, hee = [], [], []

with open("/Users/zrollins/Documents/Documents/tcrai/tcr0003/afold/num_interface_TCR_pMHC.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 3:
            t.append(float(cols[0]))
            he.append(float(cols[1]))
            hee.append(float(cols[2]))

t1, hf, hff = [], [], []

with open("/Users/zrollins/Documents/Documents/tcrai/tcr0003/modeller/num_interface_TCR_pMHC.xvg") as f:
    #lines = (line for line in f if not line.startsiwith('#') if not line.startswith('$'))
    for line in f:
        if line.startswith('#'):
            continue
        if line.startswith('@'):
            continue
        cols = line.split()

        if len(cols) == 3:
            t1.append(float(cols[0]))
            hf.append(float(cols[1]))
            hff.append(float(cols[2]))

#Statistics: One-way ANOVA with Tukey-Kramer Posthoc Test
h1 = ha + hb
h2 = hc + hd
h3 = he + hf
hbonds = {'TCR1-cfold':ha,'TCR1-modeller':hb,'TCR2-cfold':hc,'TCR2-modeller':hd,'TCR3-cfold':he,'TCR3-modeller':hf}
ST = pd.DataFrame.from_dict(hbonds, orient='index')
ST = ST.transpose()
f, p = stats.f_oneway(ST.dropna()['TCR1-cfold'],ST.dropna()['TCR1-modeller'],ST.dropna()['TCR2-cfold'],ST.dropna()['TCR2-modeller'],ST.dropna()['TCR3-cfold'],ST.dropna()['TCR3-modeller'])
print('--------------------------------------------------')
print('One-Way ANOVA: Instantaneous LJ-Contacts')
print('--------------------------------------------------')
print ('F=',f,',', 'PR(>F)=',p)

###Posthoc Tukey-Kramer Test
tk=ST[['TCR1-cfold','TCR1-modeller','TCR2-cfold','TCR2-modeller','TCR3-cfold','TCR3-modeller']].copy()
tk_melt=pd.melt(tk.reset_index(),id_vars=['index'], value_vars=['TCR1-cfold','TCR1-modeller','TCR2-cfold','TCR2-modeller','TCR3-cfold','TCR3-modeller'])
tk_melt.columns=['index','Conditions','value']
tk_melt=tk_melt.dropna()
tk_melt=tk_melt.reset_index(drop=True)
m_comp=pairwise_tukey(data=tk_melt, dv='value', effsize='cohen', between ='Conditions')
#m_comp.to_excel(writer,'LJ-Contacts')
#writer.save()