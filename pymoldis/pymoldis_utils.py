def headers():
    '''
    Prepares header content for the output

            Input:

            Returns:
                    logo (string): pymoldis logo
                    header (string): header content
    '''

    logo='''
 ┏┓  ┳┳┓  ┓┳┓• 
 ┃┃┓┏┃┃┃┏┓┃┃┃┓┏
 ┣┛┗┫┛ ┗┗┛┗┻┛┗┛
    ┛     
 A Python suite for data-mining the Quantum Chemistry Big Data 
 developed through the MolDis project (https://moldis.tifrh.res.in/)
    '''
    header='''
 Source: https://github.com/moldis-group/pymoldis
 Support e-mail: ramakrishnan@tifrh.res.in
    '''
    return logo, header

def makexyz(index,df,filename):

    import numpy as np

    mol=df.iloc[index,:]

    ele=mol['atoms']
    coord=mol['coords(Ang)']

    ele=ele.strip(']').strip('[').strip(',').split(',')
    atoms=[]
    for iele in ele:
        atoms.append(iele.strip("'"))

    coord=coord.strip(']').strip('[').strip(',').split(',')
    xyz=[]
    for icoord in coord:
        xyz.append(float(icoord.strip("'").strip(']').strip('[')))

    xyz=np.array(xyz)
    xyz=np.reshape(xyz,[len(atoms),3])

    xyzfile=open(filename,'w')

    print(len(atoms))
    xyzfile.write(str(len(atoms))+'\n')
    print(filename)
    xyzfile.write(filename+'\n')
    for i,atom in enumerate(atoms):
        print('{:s}{:15.8f}{:15.8f}{:15.8f}'.format(atom,xyz[i][0],xyz[i][1],xyz[i][2]))
        xyzfile.write('{:s}{:15.8f}{:15.8f}{:15.8f}\n'.format(atom,xyz[i][0],xyz[i][1],xyz[i][2]))

    xyzfile.close()

    return

def get_atom_prop(df,index,prop):

    import numpy as np

    mol=df.iloc[index,:]

    str_sigma=mol[prop]
    str_sigma=str_sigma.strip(']').strip('[').strip(',').split(',')
 
    sigma=[]
    for str in str_sigma:
        sigma.append(float(str))

    ele=mol['atoms']
  # coord=mol['coords(Ang)']

    ele=ele.strip(']').strip('[').strip(',').split(',')
    atoms=[]
    for iele in ele:
        atoms.append(iele.strip("'"))

  # coord=coord.strip(']').strip('[').strip(',').split(',')
  # xyz=[]
  # for icoord in coord:
  #     xyz.append(float(icoord.strip("'").strip(']').strip('[')))

  # xyz=np.array(xyz)
  # xyz=np.reshape(xyz,[len(atoms),3])

  # print(len(atoms))
  # for i,atom in enumerate(atoms):
  #     print('{:s}{:15.8f}{:15.8f}{:15.8f}{:15.8f}'.format(atom,xyz[i][0],xyz[i][1],xyz[i][2],sigma[i]))

    return atoms, sigma

def get_atoms_count(index,df):

    atoms_column = df.iloc[index]['atoms']

    all_atoms = ''.join(atoms_column)

    atom_counts = {}
    for atom in all_atoms:
        if atom in atom_counts:
            atom_counts[atom] += 1
        else:
            atom_counts[atom] = 1

    del atom_counts[',']
    del atom_counts["'"]
    del atom_counts['[']
    del atom_counts[']']

    return atom_counts

def print_MolFormula(df):
    import numpy as np

    Nmols=df['SMI'].count()

    MolForms=[]
    for imol in range(Nmols):
        atom_counts=get_atoms_count(imol,df)
        molecular_formula = ''.join([f"_{atom}{count}" for atom, count in sorted(atom_counts.items())])
        molecular_formula = molecular_formula[1:]
        MolForms.append(molecular_formula)

    unique_elements, counts = np.unique(MolForms, return_counts=True)

    sorted_indices = np.argsort(counts)[::-1]
    sorted_elements = unique_elements[sorted_indices]
    sorted_counts = counts[sorted_indices]

    for item, frequency in zip(sorted_elements, sorted_counts):
        print(f"Item: {item}, Frequency: {frequency}")

    return

def get_ConstitutionalIsomers(df,Formula):

    Nmols=df['SMI'].count()

    MolForms=[]

    for imol in range(Nmols):
        atom_counts=get_atoms_count(imol,df)
        molecular_formula = ''.join([f"_{atom}{count}" for atom, count in sorted(atom_counts.items())])
        molecular_formula = molecular_formula[1:]
        MolForms.append(molecular_formula)

    MolIndices=[]
    for iform, MolForm in enumerate(MolForms):
        if MolForm==Formula:
            MolIndices.append(iform)

    return MolIndices

def readxyz(xyz_file):

    import numpy as np
    import pymoldis as pym

    mol_R = []
    mol_Z = []

    iline = 0

    with open(xyz_file,'r') as file:
        lines = file.readlines()
    file.close()

    for i in range(np.size(lines)):

        line = lines[i].split()

        if iline == 0:
            N_atom = int(line[0]) # Number of atoms present in the molecule

        if iline == 1:
            mol_title = line[0] # Name of the molecule

        if iline > 1:

            element = line[0]
            z = pym.atomic_number(element)
            mol_Z.append(z)

            ri = [float(line[1]),float(line[2]),float(line[3])] # coordinate of atom i
            ri = np.array(ri)
            mol_R.append(ri)

        iline=iline+1

    return mol_Z, mol_R
