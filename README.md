# vina_demo
A demo and tutorial for Autodock Vina

## Setup
 
If you haven't already, install the latest version of the Anaconda Python distribution [conda](https://docs.conda.io/projects/conda/en/stable/), or [miniconda](https://docs.anaconda.com/free/miniconda/).

NOTE: The installation package is a large `*.sh` file 
[https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh].
You can either download this to your local machine and `scp` to Owlsnest, or download it directly using `wget`.


### Create a conda environment for the vina work

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

###



