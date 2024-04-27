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

    xyzfile=open('filename','w')

    print(len(atoms))
    xyzfile.write(str(len(atoms)))
    print(filename)
    xyzfile.write(filename)
    for i,atom in enumerate(atoms):
        print('{:s}{:15.8f}{:15.8f}{:15.8f}'.format(atom,xyz[i][0],xyz[i][1],xyz[i][2]))
        xyzfile.write('{:s}{:15.8f}{:15.8f}{:15.8f}'.format(atom,xyz[i][0],xyz[i][1],xyz[i][2]))

    xyzfile.close()

    return

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
