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
* pandas

```
conda install -c conda-forge -c bioconda mgltools openbabel zlib --yes
conda install pandas
```

If you don't already have `wget` installed (use `which wget` to check), install it:

```
pip install wget
```

###  Next Steps

1. Follow the instructions in the `runme_setup` document to prepare the receptor
2. Prepare the ligands using `python prepare_ligands.py` 
3. Dock the ligands using `docking.py`
4. Visualize the docking results in ChimeraX
5. Analyze the Vina score vs. RMSD-to-xtal using `python analysis.py`


### References

Heavily inspired by https://colab.research.google.com/github/pb3lab/workshops/blob/main/tutorials/spb2022/D1_Tutorial2.ipynb#scrollTo=LRlv9MqoCC19 





