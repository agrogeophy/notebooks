#!/usr/bin/env python
# coding: utf-8

# # Monitoring of drying under winter wheat by ERT
# This notebook shows how time-lapse electrical resistivity tomography (ERT) can help to follow the soil drying (mainly attributed to root water uptake) during the growth season.
# 
# This dataset was collected on 24 pins array (0.25 m electrode spacing) using a dipole-dipole sequence with a Syscal Pro 48 (Iris Instruments, Orléans, France). The experiment took place at Worburn (UK), a research station managed by Rothamsted Research in 2017 under winter wheat.

# In[ ]:


import matplotlib.pyplot as plt
from resipy.R2 import R2
import os
print(os.getcwd())
datadir = '../data/blanchy/dc-2d-timelapse/data/'
print


# In[ ]:


k = R2() # initiate an R2 instance
k.createTimeLapseSurvey([datadir + '17031501.csv',
                         datadir + '17040301.csv',
                         datadir + '17051601.csv'], ftype='Syscal')
k.filterUnpaired() # remove dummy quadrupoles added to make dipole-dipole faster


# In[ ]:


fig, axs = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
ax = axs[0]
k.showPseudo(index=0, ax=ax, vmin=30, vmax=80)
ax.set_title('(a) 2017-03-15')
ax.set_xlabel('')
ax = axs[1]
k.showPseudo(index=1, ax=ax, vmin=30, vmax=80)
ax.set_title('(b) 2017-04-03')
ax.set_xlabel('')
ax = axs[2]
k.showPseudo(index=2, ax=ax, vmin=30, vmax=80)
ax.set_title('(c) 2017-05-16')


# In[ ]:


k.fitErrorPwl(index=-2) # fit a power-law error model for all dataset aggregated


# In[ ]:


k.createMesh(typ='trian', cl=0.02, cl_factor=20, show_output=False) # create a triangular mesh with a characteristic length of 0.5
k.showMesh() # display the mesh


# In[ ]:


k.invert(parallel=True) # run the inversion (and write R2.in and protocol.dat automatically)


# In[ ]:


fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
ax = axs[0]
ax.set_title('(a) 15th March to 3rd April')
k.showResults(ax=ax, index=1, attr='difference(percent)', vmin=0, vmax=50, sens=False)
ax.set_xlabel(None)
ax = axs[1]
ax.set_title('(b) 15th March to 16th May')
k.showResults(ax=ax, index=2, attr='difference(percent)', vmin=0, vmax=50, sens=False)
fig.tight_layout()


# In[ ]:




