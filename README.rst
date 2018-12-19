===================
Schrodinger_Project
===================
.. image:: https://coveralls.io/repos/github/JinyuXu/schrodinger_project/badge.svg?branch=master
        :target: https://coveralls.io/github/JinyuXu/schrodinger_project?branch=master

.. image:: https://img.shields.io/pypi/v/schrodinger_project.svg
        :target: https://pypi.python.org/pypi/schrodinger_project

.. image:: https://img.shields.io/travis/JinyuXu/schrodinger_project.svg
        :target: https://travis-ci.org/JinyuXu/schrodinger_project

.. image:: https://readthedocs.org/projects/schrodinger-project/badge/?version=latest
        :target: https://schrodinger-project.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


This progject aims for solving the stationary schrodinger equation with Fourier basis set.

* Free software: MIT license
* Documentation: https://schrodinger-project.readthedocs.io.


Features
--------

* Installation: git clone git@github.com:JinyuXu/schrodinger_project.git
                pip install schrodinger_project
* Usage: This programme takes 3 inputs: potential energy V_0(x), c and the size of basis set
* Example: python schrodinger_project.py --data_table [[0,0],[1.57079,6],[3.14159,0]] --c 1 --basis_size 3
* Note: please convert all pi in the data table into float.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
