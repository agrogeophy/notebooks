#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# 
# # Inversion of current source density apply to a roots imaging
# 
# 

# In[ ]:


import os
import matplotlib.pyplot as plt

# import numpy as np

# maindir='E:/Padova/Software/SourceInversion/icsd_dev/'
# os.chdir(maindir)

# -----------------------------------#
# Exemple cotton
# -----------------------------------#
# path2files="examples/Cotton_Soil/Nail1/"
path2files="./nail1/"

# path2files = os.path.join(os.path.dirname('__file__'), '/Cotton_Soil/Nail1/')
# cwd=os.getcwd()

# path2files= '../examples/nail1/'
# DIR= cwd + path2files

# os.chdir(DIR)
# path2files = 
# fname = os.path.join(cwd, path2files)

# from icsd2d_class import iCSD2d_Class as i2d
# icsd=i2d(dirName=path2files)   
# icsd.icsd_init()

# # 
# icsd.wr=1 #weight regularization
# icsd.run_single()
# icsd.run_pareto()

# -----------------------------------#
# apply here a smallness contrainst to the regularisation
from icsd3d_class import iCSD3d_Class as i3d
from plotters import mpl_plot

# mpl_plot.showObs2d(path2files)


# import iCSD3d_Class as i3d

icsd=i3d(dirName=path2files)   
icsd.type='2d'
icsd.obs_err='sqrt' # choose between constant weight and w = 1/sqrt(abs(obs))
icsd.wr=1 #weight regularization
icsd.alphaSxy=True
icsd.x0_prior=True
icsd.x0_ini_guess=True # initial guess
icsd.icsd_init()


icsd.estimateM0(methodM0='F1',show=True)

# icsd.clim=[0,0.1]
# icsd.run_single()

sol= icsd.invert()
# icsd.invert(pareto=True, regMesh='strc',x0_prior=True, 
#             pareto_MinErr=1, pareto_MaxErr=100)


 
fig, ax = plt.subplots()
ax.scatter([0.2,0.4],[0.1,0.3],color='r',marker='v')
icsd.showResults(ax=ax)
# fig, ax = plt.subplots()
plt.show()


icsd.showResults()

# icsd.ModelResolution(jacMi=305)

# # run pareto
# icsd.pareto_MinErr=0.001
# icsd.pareto_MaxErr=1
# icsd.pareto_nSteps=3

# icsd.knee=True
# icsd.run_pareto()

