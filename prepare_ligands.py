import os, sys
import pandas as pd
df = pd.read_csv('input_files/Adeshina_2020_smiles.csv')

"""This looks like:

ligand,SMILES
AC1,COC=1C=CC=C2NC=C(CCNC(C)C=3C=CC(=CC3)N4C=NC=N4)C12
AC2,CN1N=C(C=C1NC(=O)C=2C=NC=C(C2)C=3C=CC(Cl)=CC3)C(C)(C)C
AC3,CC=1C=CC=C(C1)C=2C=NC=C(C2)C(=O)NC3=NC(=CS3)C4CCNCC4
...
"""

df2 = pd.read_csv('input_files/human_AChE_binders.csv')
"""
ligand,SMILES
donezepil,COC1=C(C=C2C(=C1)CC(C2=O)CC3CCN(CC3)CC4=CC=CC=C4)OC
huperzine,CC=C1C2CC3=C(C1(CC(=C2)C)N)C=CC(=O)N3
galantamine,CN1CCC23C=CC(CC2OC4=C(C=CC(=C34)C1)OC)O
"""


prepare_ligand4 = '~/anaconda3/envs/vina/bin/prepare_ligand4.py'

def run_cmd(cmd, testing=False):
    """Run a shell command on the UNIX command line.

    OPTIONS
    testing          If True, just print the cmd. Default: False
    """

    print('>>', cmd)
    if not testing:
        os.system(cmd)

# Create a series of directories containing each ligand
ligand_list = []
#ligand_list += [str(df.loc[index,'ligand']) for index, row in df.iterrows()]
ligand_list += [str(df2.loc[index,'ligand']) for index, row in df2.iterrows()]

smiles_list = []
#smiles_list += [str(df.loc[index,'SMILES']) for index, row in df.iterrows()]
smiles_list += [str(df2.loc[index,'SMILES']) for index, row in df2.iterrows()]

for i in range(len(smiles_list)):

    ligand = ligand_list[i]
    smiles = smiles_list[i]
    print(f"{ligand}, {smiles} ")

    ligdir = f'./{ligand}'
    if not os.path.exists(ligdir):
        os.mkdir(ligdir)

    # Write the ligand to file
    smilesfile = os.path.join(ligdir, f'{ligand}.smiles')
    fout = open(smilesfile, 'w')
    fout.write(smiles)
    fout.close()
    print(f'Wrote: {smilesfile}')

    # Use OpenBabel to convert the SMILES into a 3D MOL2 format and
    # perform a weighted rotor search for lowest energy conformer
    mol2file = smilesfile.replace('.smiles','.mol2')
    os.system(f'obabel {smilesfile} -O {mol2file} --gen3d --best --canonical --conformers --weighted --nconf 50 --ff GAFF')
    print(f'  ...  {mol2file}')

    # Then, prepare ligands for docking using the Autodock script
    pdbqtfile = smilesfile.replace('.smiles','.pdbqt')

    ### ... for some reason the script does not work with files on other directories
    os.chdir(ligdir)
    local_mol2file = os.path.basename(mol2file)
    local_pdbqtfile = os.path.basename(pdbqtfile)
    cmd = f'python2 {prepare_ligand4} -l {local_mol2file} -o {local_pdbqtfile} -U nphs_lps -v'
    run_cmd(cmd)  #, testing=True)
    print(f'  ...  {pdbqtfile}')
    os.chdir('../')




