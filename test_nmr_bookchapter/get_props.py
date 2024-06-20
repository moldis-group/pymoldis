import pymoldis as pym

df=pym.get_data('bigqm7w_nmr_dftgeoms')
Nmol=len(df)

props=['wB97XD/def2TZVP', 'MP2/cc-pVDZ', 'MP2cc-pVTZ', 'CCSD/cc-pVDZ', 'CCSD/cc-pVTZ-est', 'CCSD(T)/cc-pVDZ', 'CCSD(T)/cc-pVTZ-est']
gprops=['wB97XD_TZVP', 'MP2_VDZ', 'MP2_VTZ', 'CCSD_VDZ', 'CCSD_VTZ', 'CCSDT_VDZ', 'CCSDT_VTZ']

eles=['H','C','N','O','F']

for ele in eles:
    for prop in gprops:
        prop_file=open(ele+'_'+prop+'.dat','w')
        prop_file.close()

for imol in range(Nmol):

    for ele in eles:

        for iprop, prop in enumerate(props):

            atoms,sigma=pym.get_atom_prop(df,imol,prop)

            prop_file=open(ele+'_'+gprops[iprop]+'.dat','a')
       
            for iatom, at in enumerate(atoms):
                #print(at, iatom, ele,sigma, sigma[0])
                if at == ele:
                    val=float(sigma[iatom])
                    print(val)
                    prop_file.write('{:25.16f}'.format(val))
                    prop_file.write('\n')
          
       
prop_file.close()
