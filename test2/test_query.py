import pymoldis as pym

df=pym.get_data('bigqm7w_nmr_dftgeoms')

print(df.describe())

# properties
print(df.keys())
#Index(['Molecule_number', 'SMI', 'Natoms', 'atoms', 'coords(Ang)',
#       'wB97XD/def2TZVP', 'MP2/cc-pVDZ', 'MP2cc-pVTZ', 'CCSD/cc-pVDZ',
#       'CCSD/cc-pVTZ-est', 'CCSD(T)/cc-pVDZ', 'CCSD(T)/cc-pVTZ-est'],
#      dtype='object')


# make an xyz file
xyzfile=pym.makexyz(0,df,'0_DFT.xyz')

# shielding from a level


prop='wB97XD/def2TZVP'

Nmol=len(df)
#for imol in range(Nmol):
for imol in range(2):

    atoms, sigma=pym.get_atom_prop(df,imol,prop)
    print(sigma)

    for iatm, atom in enumerate(atoms):
        print(iatm, atom)


desc = pym.descriptor_gen('C', '0_DFT.xyz', 'acm')
print(desc)
#desc = pym.descriptor_gen('H', '0_DFT.xyz', 'acm')
#print(desc)
