import os, sys, subprocess

def run_cmd(cmd, testing=False):
    """Run a shell command on the UNIX command line.

    OPTIONS
    testing          If True, just print the cmd. Default: False
    """

    print('>>', cmd)
    if not testing:
        os.system(cmd)


Download_DockRMSD = False

if (Download_DockRMSD):
    run_cmd('wget https://seq2fun.dcmb.med.umich.edu//DockRMSD/DockRMSD.gz')
    run_cmd('gunzip DockRMSD.gz')
    run_cmd('chmod +x ./DockRMSD')

# convert the xtal structure pose to mol2
run_cmd('cat input_files/4ey7_chainA.pdb | grep E20 > input_files/donepezil_xtal.pdb')
run_cmd('obabel input_files/donepezil_xtal.pdb  -O input_files/donepezil_xtal.mol2 --ff GAFF')

# convert our docking poses to mol2
run_cmd('obabel donepezil/donepezil_out.pdbqt -O donepezil/donepezil_out.mol2 -m')

########################
# ANALYSIS: docking score versus RMSD-to-xtal

# To get the docking score(s), we need to parse the [ligand]_out.pdbqt file
vina_scores = []
fin = open('donepezil/donepezil_out.pdbqt', 'r')
lines = fin.readlines()
fin.close()

for line in lines:
    if line.count('REMARK VINA RESULT:') > 0:
        # line looks like 'REMARK VINA RESULT:   -11.391      0.000      0.000'
        score = float(line.split()[3])
        vina_scores.append( score )
print('vina_scores', vina_scores)


# To get the rmsd-to-xtal of the docked pose, we need to parse the output of DockRMSD
posed_mol2files = [f'donepezil/donepezil_out{i}.mol2' for i in range(1,10)]
rmsd_values = []
for posed_mol2file in posed_mol2files:

    # Create a subprocess to run the 'ls' command
    xtal_mol2 = 'input_files/donepezil_xtal.mol2'
    output = subprocess.check_output(['./DockRMSD', xtal_mol2, posed_mol2file], text=True)

    # parse the RMSD from the line "Calculated Docking RMSD: ##.###\n" 
    lines = [line for line in output.split('\n') if line.count("Calculated Docking RMSD:") > 0]
    rmsd = float(lines[0].strip().split()[-1])
    rmsd_values.append(rmsd)
print('rmsd_values', rmsd_values)
print()

print('RMSD-to-xtal (A), Vina score (kcal/mol)')
for i in range(len(vina_scores)):
    print(f'{rmsd_values[i]},{vina_scores[i]}')
