import os, sys
from shutil import copyfile

def run_cmd(cmd, testing=False):
    """Run a shell command on the UNIX command line.

    OPTIONS
    testing          If True, just print the cmd. Default: False
    """

    print('>>', cmd)
    if not testing:
        os.system(cmd)


# Ligand directories
ligdirs = [f'AC{i}' for i in range(1,24) ]

# NOTE: the mean xyz coords for donezepil in 4ey7_chainA.pdb is -14.1,-43.8,27.7
center_x, center_y, center_z = -14.1, -43.8, 27.7   # Angstrom
size_x, size_y, size_z = 30, 30, 30

for lig in ligdirs:

    receptor = 'receptor.pdbqt'
    ligand   = os.path.join(lig, f'{lig}.pdbqt')

    config_file = os.path.join(lig, "config_singledock")

    with open(config_file, "w") as f:
        f.write(f"""# CONFIGURATION FILE

# INPUT OPTIONS 
receptor = {receptor}
ligand = {ligand}
# flex = [flexible residues in receptor in pdbqt format] 

# SEARCH SPACE CONFIGURATIONS 
# Center of the box (coordinates x, y and z 
center_x = {center_x}
center_y = {center_y}
center_z = {center_z}
# Size of the box (dimensions in x, y and z) 
size_x = {size_x}
size_y = {size_y}
size_z = {size_z}

# OUTPUT OPTIONS 
# out = [outfile]
# log = [logfile]

# OTHER OPTIONS 
# cpu = [value] # more cpus reduces the computation time
# exhaustiveness = [value] # search time for finding the global minimum, default is 8
# num_modes = [value] # maximum number of binding modes to generate, default is 9
# energy_range = [value] # maximum energy difference between the best binding mode and the worst one displayed (kcal/mol), default is 3
# seed = [value] # explicit random seed, not required
    """)

    cmd = f'./vina --config {config_file}'
    run_cmd(cmd, testing=True)
