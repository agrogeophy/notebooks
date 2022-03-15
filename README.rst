.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/agrogeophy/notebooks/master?filepath=notebooks
 
.. image:: https://img.shields.io/badge/Slack-agrogeophy-1.svg?logo=slack
 :target: https://agrogeophy.slack.com/ 

.. image:: https://zenodo.org/badge/292793548.svg
   :target: https://zenodo.org/badge/latestdoi/292793548
  
  
********************
Agrogeophy-notebooks
********************
A collection of jupyter notebooks that use agrogeophysical models. To view the notebooks, checkout **https://agrogeophy.github.io/notebooks/auto_examples/index.html**

Agrogeophy-notebooks is part of the `agrogeophysical catalog website <http://geo.geoscienze.unipd.it/growingwebsite/map_catalog>`__ 


How to run the notebooks
========================


The notebooks can be run online through Binder, or downloaded and run locally.

1. Launch the binder
2. Select the notebook of interest from the contents
3. Run the Jupyter notebook


*****************
How to contribute
*****************



Notebook structure
==================


We have developed a common framework in which each survey history is presented: 

- Contributors
   - author name 
   - reviewer name
- Context
- Materials and Methods
- Results

Submit a new notebook
=====================

Create a pull request on this repository.

- the new notebook (.ipynb) should be added to the 'notebooks' folder
- the data for the notebook (if any) should be added to the 'data' folder
- if the notebook requires specific packages, add them by editing 'requirements.txt' and 'apt.txt'

The notebooks will be automatically build when the pull request is merged with the master branch. The Action (main.yml) will use 'sphinx-build' to build a gallery of examples and automatically publish the results on the Github Pages.



*************
Useful links
*************

How to share your notebooks? 
============================

`Binder + Zenodo by blog jupyter <https://blog.jupyter.org/binder-with-zenodo-af68ed6648a6>`_

`Sharing and Publishing Jupyter Notebooks from reprocible science <https://reproducible-science-curriculum.github.io/publication-RR-Jupyter/aio.html>`_

*************
Contributors
*************

- Benjamin Mary, UNIPD
- Guillaume Blanchy, University of Lancaster

We welcome any feedback and ideas!
Let us know by submitting 
`issues on Github <https://github.com/agrogeophy/notebooks/issues>`__
or send us a message on our
`Slack chatroom <https://agrogeophy.slack.com/>`__.
