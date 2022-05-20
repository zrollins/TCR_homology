#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 22:46:15 2022

@author: zrollins
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:08:54 2022

@author: zrollins
"""


#H-Frequency
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib.pyplot as plt
from pingouin import pairwise_tukey
from pingouin import pairwise_tukey
from openpyxl import load_workbook

df = pd.read_excel (r'/Users/zrollins/Documents/Documents/tcrai/tcr0001/afold/cfrequency.xlsx')
df2 = pd.read_excel (r'/Users/zrollins/Documents/Documents/tcrai/tcr0001/modeller/cfrequency.xlsx')
#df2 = pd.read_excel (r'/Users/zrollins/Documents/Documents/tcrai/tcr0001/cfrequency.xlsx')
df5 = pd.read_excel (r'/Users/zrollins/Documents/Documents/tcrai/tcr0002/afold/cfrequency.xlsx')
df6 = pd.read_excel (r'/Users/zrollins/Documents/Documents/tcrai/tcr0002/modeller/cfrequency.xlsx')
#df6 = pd.read_excel (r'/Users/zrollins/Documents/Documents/tcrai/tcr0002/cfrequency.xlsx')
df9 = pd.read_excel (r'/Users/zrollins/Documents/Documents/tcrai/tcr0003/afold/cfrequency.xlsx')
df10 = pd.read_excel (r'/Users/zrollins/Documents/Documents/tcrai/tcr0003/modeller/cfrequency.xlsx')
#df10 = pd.read_excel (r'/Users/zrollins/Documents/Documents/tcrai/tcr0003/cfrequency.xlsx')



#TCR1
#df['TCR1-Colabfold'] = pd.Series(df2['H-Bond Frequency (TCR-pMHC)'])
#df['100 ns Total Time (ps)'] = pd.Series(df2['Total Time (ps)'])

#TCR2
#df5['100 ns H-Bond Frequency (pMHC)'] = pd.Series(df6['H-Bond Frequency (pMHC)'])
#df5['100 ns Total Time (ps)'] = pd.Series(df6['Total Time (ps)'])


#TCR3
#df9['100 ns H-Bond Frequency (pMHC)'] = pd.Series(df10['H-Bond Frequency (pMHC)'])
#df9['100 ns Total Time (ps)'] = pd.Series(df10['Total Time (ps)'])
win=25
df.fillna(0, inplace=True)
df['LJ-Contact Frequency (TCR-pMHC) SMA']= df.iloc[:,2].rolling(window=win).mean()*25
df2.fillna(0, inplace=True)
df2['LJ-Contact Frequency (TCR-pMHC) SMA']= df2.iloc[:,2].rolling(window=win).mean()*25
df5.fillna(0, inplace=True)
df5['LJ-Contact Frequency (TCR-pMHC) SMA']= df5.iloc[:,2].rolling(window=win).mean()*25
df6.fillna(0, inplace=True)
df6['LJ-Contact Frequency (TCR-pMHC) SMA']= df6.iloc[:,2].rolling(window=win).mean()*25
df9.fillna(0, inplace=True)
df9['LJ-Contact Frequency (TCR-pMHC) SMA']= df9.iloc[:,2].rolling(window=win).mean()*25
df10.fillna(0, inplace=True)
df10['LJ-Contact Frequency (TCR-pMHC) SMA']= df10.iloc[:,2].rolling(window=win).mean()*25
print(df10)
print(df10)
#print(df)
#print(df5)
#print(df9)

ax = plt.gca()
df.plot(kind='line',x='TCR-pMHC', y='LJ-Contact Frequency (TCR-pMHC) SMA', ls='--', color='lime', ax=ax)
df2.plot(kind='line',x='TCR-pMHC', y='LJ-Contact Frequency (TCR-pMHC) SMA', color='lime', ax=ax)
df5.plot(kind='line',x='TCR-pMHC', y='LJ-Contact Frequency (TCR-pMHC) SMA', ls='--', color='magenta', ax=ax)
df6.plot(kind='line',x='TCR-pMHC', y='LJ-Contact Frequency (TCR-pMHC) SMA', color='magenta', ax=ax)
df9.plot(kind='line',x='TCR-pMHC', y='LJ-Contact Frequency (TCR-pMHC) SMA', ls='--', color='blue', ax=ax)
df10.plot(kind='line',x='TCR-pMHC', y='LJ-Contact Frequency (TCR-pMHC) SMA', color='blue', ax=ax)
ax.set_ylabel(r'Probability Density ($\frac{1}{Number}$)', fontname='Arial', fontsize='20')
ax.set_xlabel('Number of LJ Contacts', fontname='Arial', fontsize='20')
#ax.set_xticklabels(['0.0','0.0','100','200','300','400', '500','600'],fontname='Arial')
#ax.set_yticklabels(['0.00','0.00','0.05','0.10','0.15','0.20','0.25'],fontname='Arial')
ax.legend(['TCR1-ColabFold', 'TCR1-Modeller','TCR2-ColabFold','TCR2-Modeller', 'TCR3-ColabFold','TCR3-ColabFold'])
#ax.legend(['TCR1', 'TCR2', 'TCR3'])
#ax.legend(['EQ','GVA'])
#ax.set_title('TCR-pMHC Hydrogen Bonding', fontname='Arial', fontsize='20')
plt.rc('xtick',labelsize=15)
plt.rc('ytick',labelsize=15)
plt.savefig('/Users/zrollins/Documents/Documents/tcrai/cfreq_compare.png', figsize=(6,4),bbox_inches='tight',dpi=300)
plt.show()

#print(df)

