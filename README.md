# Python Plotting 
This repository contains the tutorial "Python Plotting " which is part of the 2021 GHSC HazDev Summer Python Tutorial Series.

Please use Binder via the link below to launch this tutorial in your web browser:

https://mybinder.org/v2/gh/mhearne-usgs/python_plotting.git/main?filepath=python_plotting_introduction.ipynb

If you prefer to run the notebook locally, clone the repository:

`git clone git@github.com:mhearne-usgs/python_plotting.git`

 and run the following commands in the top level of the repository:

(on Mac or Linux)
- `bash install.sh`

on Windows:
- `conda create -n plotting_tutorial python>=3.6 jupyter ipython matplotlib numpy cartopy pandas -y`
- `conda activate plotting_tutorial`
- `jupyter notebook python_plotting_introduction.ipynb`

\*Note: Anaconda or Miniconda must be installed first

- https://docs.anaconda.com/anaconda/install/
- https://docs.conda.io/en/latest/miniconda.html

## The topics covered include:
- Anatomy of a Matplotlib plot
- Introduction to Pandas for reading in data
- Plot histograms
- Plot error bars and continuous error bars
- Plot data as an image
- ColorMaps
- Cartopy
- Subplot
