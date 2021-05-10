Getting Started
===============

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/agrogeophy/notebooks/master?filepath=notebooks
 
.. image:: https://img.shields.io/badge/Slack-agrogeophy-1.svg?logo=slack
 :target: https://agrogeophy.slack.com/
  
.. image:: https://zenodo.org/badge/292793548.svg
   :target: https://zenodo.org/badge/latestdoi/292793548

Agrogeophy-notebooks is a curated repository of interactive agrogeophysical notebooks, seamlessly integrating data, text, code and figures. Notebooks can be freely modified and re-executed through the web, offering a fully reproducible, “libre” path from data to figures. Agrogeophy-notebooks is powered by the Binder project.To view the notebooks, checkout the Gallery of examples.

About
-----
Agrogeophy-notebooks is part of the `agrogeophysical catalog website <http://geo.geoscienze.unipd.it/growingwebsite/map_catalog>`__ 


What can be published on CAGS-notebooks?
----------------------------------------
Agrogeophy-notebooks currently welcomes submissions along two tracks:

- Tutorial notebooks related to a workshop/conference in the agroeophysic field.
- Companion notebooks for articles in the agroeophysic field.
These notebooks are expected to use less than 100 GB disk space, and run in less of an hour, although exceptions may be granted on a case by case basis.

How are CAGS-notebooks submissions reviewed?
--------------------------------------------
The CAGS team checks that the notebooks fit one of the two tracks above, run correctly, and that the text and code are readable.


How to contribute
-----------------
Submit a new notebook via the official website and create a pull request on this repository.

#. the new notebook (.ipynb) should be added to the 'notebooks' folder
#. the data for the notebook (if any) should be added to the 'data' folder
#. if the notebook requires specific packages, add them by editing 'requirements.txt' and 'apt.txt'
#. add metadata descriptors for your notebook by filling the `online form <https://agrogeophy.github.io/catalog/input_form.html>`__.

The notebooks will be automatically build when the pull request is merged with the master branch. The Action (main.yml) will use 'sphinx-build' to build a gallery of examples and automatically publish the results on the Github Pages.


Contributors
------------
- Guillaume Blanchy, University of Lancaster


Citing 
------
If you use agrogeophy-notebooks for you work, please cite this paper as:

.. image:: https://zenodo.org/badge/292793548.svg
   :target: https://zenodo.org/badge/latestdoi/292793548

BibTex code::

	@software{benjamin_mary_2020_4164938,
	  author       = {Benjamin Mary and
	                  Guillaume Blanchy},
	  title        = {{A collection of jupyter notebooks that use 
	                   agrogeophysical models}},
	  month        = oct,
	  year         = 2020,
	  publisher    = {Zenodo},
	  version      = {v0.1},
	  doi          = {10.5281/zenodo.4164938},
	  url          = {https://doi.org/10.5281/zenodo.4164938}
	}


Get involved 
------------
We welcome any feedback and ideas!
Let us know by submitting 
`issues on Github <https://github.com/agrogeophy/notebooks/issues>`__
or send us a message on our
`Slack chatroom <https://agrogeophy.slack.com/>`__.
