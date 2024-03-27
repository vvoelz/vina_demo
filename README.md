# vina_demo
A demo and tutorial for Autodock Vina

## Setup

If you haven't already, install the latest version of Anaconda Python 3.

Create a conda environment for the vina work:

```
conda create --name vina
conda activate vina
```

And install the following packages:
* bioconda
* mgltools
* openbabel
* zlib

```
conda install -c conda-forge -c bioconda mgltools openbabel zlib --yes
```

If you don't already have `wget` installed (use `which wget` to check), install it:

```
pip install wget
```





