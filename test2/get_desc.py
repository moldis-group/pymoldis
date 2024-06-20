import pymoldis as pym

df=pym.get_data('bigqm7w_nmr_uffgeoms')
Nmol=len(df)

#eles=['H','C','N','O','F']
eles=['F']
reps=['acm', 'bob0', 'bob1', 'bob2', 'bob3', 'bob4']


for ele in eles:
    for rep in reps:
        desc_file=open(ele+'_'+rep+'.dat','w')
        desc_file.close()

for imol in range(Nmol):
       
    xyzfile=pym.makexyz(imol,df,'mol.xyz')

    for ele in eles:

        for rep in reps:

            desc_file=open(ele+'_'+rep+'.dat','a')
       
            desc = pym.descriptor_gen(ele, 'mol.xyz', rep)
       
            for at_desc in desc:
       
                for idesc in at_desc:
                    desc_file.write('{:25.16f}'.format(idesc))
                desc_file.write('\n')
       
            desc_file.close()
