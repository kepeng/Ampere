

<!--
[![Build Status](https://travis-ci.org/ECSHackWeek/impedance.py.svg?branch=master)](https://travis-ci.org/ECSHackWeek/impedance.py)

[![Coverage Status](https://coveralls.io/repos/github/ECSHackWeek/impedance.py/badge.svg?branch=master)](https://coveralls.io/github/ECSHackWeek/impedance.py?branch=master)

[![Documentation Status](https://readthedocs.org/projects/impedancepy/badge/?version=latest)](https://impedancepy.readthedocs.io/en/latest/?badge=latest)
-->


Ampere - Advanced Model Package for ElectRochemical Experiments
------------

`Ampere` is a Python module for working with battery models.

Using a [scikit-learn-like API](https://arxiv.org/abs/1309.0238), we hope to make visualizing, fitting, and analyzing impedance spectra more intuitive and reproducible.

<i>Ampere is currently in the alpha phase and new features are rapidly being added.</i>
If you have a feature request or find a bug, please feel free to [file an issue](https://github.com/nealde/Ampere/issues) or, better yet, make the code improvements and [submit a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)! The goal is to build an open-source tool that the entire electrochemical community can improve and use!

Ampere currently provides:
- a simple API for fitting, predicting, and plotting discharge curves
- A simple API for generating data, or fitting with arbitrary charge / discharge patterns.


### Installation
#### Dependencies

Ampere requires:

- Python (>=3.5)
- SciPy (>=1.0)
- NumPy (>=1.14)
- Matplotlib (>=2.0)
- Cython (>=0.29)


Several example notebooks are provided in the examples/ directory. Opening these will require Jupyter notebook or Jupyter lab.

#### User Installation

The easiest way to install Ampere is using pip:

`pip install ampere`

#### Examples and Documentation

Several examples can be found in the `examples/` directory (the [fitting_tutorial.ipynb](https://github.com/ECSHackWeek/impedance.py/blob/master/examples/fitting_tutorial.ipynb) is a great place to start) and the documentation can be found at [impedancepy.readthedocs.io](https://impedancepy.readthedocs.io/en/latest/).
