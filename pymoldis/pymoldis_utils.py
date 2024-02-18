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
    xyz=np.reshape(xyz,[4,3])

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
