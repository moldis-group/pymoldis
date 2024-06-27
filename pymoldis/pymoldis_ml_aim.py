import numpy as np
import sys
from pymoldis import atomic_number
from pymoldis import readxyz

def acm(max_atom,target_atom, mol_Z, mol_R):

    dim = 23 
    N = np.size(mol_Z) 
    
    indices=[]

    for i in range(N):
        distances = []
        for j in range(N):
            if i != j:
                distance = np.linalg.norm(mol_R[i] - mol_R[j])
                distances.append((j, distance))

        distances.sort(key=lambda x: x[1], reverse=False)

        indi=[]
        indi.append(i)

        if max_atom <= dim:
            for m in range(N-1): 
                indi.append(distances[m][0])

        if max_atom > dim:
            for m in range(dim-1):    # First element is i itself, so 23-1 = 22 nearest elements
                indi.append(distances[m][0])

        indices.append(indi)


    desc=[]
    
    for k in range(N):
        if mol_Z[k] == atomic_number(target_atom):
            acm = np.zeros( [dim,dim] )

            for i1,i in enumerate(indices[k]):

                for j1,j in enumerate(indices[k]):

                    rij = np.linalg.norm(mol_R[i] - mol_R[j])

                    if i == j:
                        acm[i1][i1] = 0.5*mol_Z[i]**2.4
                    else:
                        acm[i1][j1] = mol_Z[i]*mol_Z[j]/rij
                        
            vec = []

            for i in range(dim):
                for j in range(i,dim):
                    vec.append(acm[i][j])
            desc.append(vec)

    return np.array(desc)

def bob(bob_N,target_atom,mol_Z,mol_R):

    def find_index(number, data, i):
        index = []

        ri = np.array([data[i][1],data[i][2],data[i][3]])
        distances = []

        for j in range(number):
            rj = np.array([data[j][1],data[j][2],data[j][3]])
            if i != j:
                distance = np.linalg.norm(ri-rj)
                distances.append((j, distance))

        distances.sort(key = lambda x: x[1])

        for j,distance in distances:
            index.append(j)
        return index 

    def construct_bag(number, data, i, delete):
        index = []
        bag = []

        zi = float(data[i][0])
        ri = np.array([data[i][1],data[i][2],data[i][3]])

        bag_11 = []   # HH   
        bag_66 = []   # CC     
        bag_77 = []   # NN    
        bag_88 = []   # OO    
        bag_99 = []   # FF    
        bag_16 = []   # HC  
        bag_17 = []   # HO   
        bag_18 = []   # HN  
        bag_19 = []   # HF  
        bag_67 = []   # CO  
        bag_68 = []   # CN  
        bag_69 = []   # CF    
        bag_78 = []   # NO  
        bag_79 = []   # NF    
        bag_89 = []   # OF

        distances = []

        for j in range(number):

            zj = float(data[j][0])
            rj = np.array([data[j][1],data[j][2],data[j][3]])

            if i != j:
                distance = np.linalg.norm(ri-rj)
                distances.append((j, distance))

        distances.sort(key = lambda x: x[1])

        for j,distance in distances:
            index.append(j)

        for j in index:
            if j not in delete:
                zj = float(data[j][0])
                rj = np.array([data[j][1],data[j][2],data[j][3]])

                rij = np.linalg.norm(ri-rj)
                val = ( zi * zj ) / rij

                if zi == 1:
                    if zj == 1: 
                        if np.size(bag_11) < bag_11_len: bag_11.append(val)
                    if zj == 6: 
                        if np.size(bag_16) < bag_16_len: bag_16.append(val)
                    if zj == 7: 
                        if np.size(bag_17) < bag_17_len: bag_17.append(val)
                    if zj == 8: 
                        if np.size(bag_18) < bag_18_len: bag_18.append(val)
                    if zj == 9: 
                        if np.size(bag_19) < bag_19_len: bag_19.append(val)

                if zi == 6: 
                    if zj == 1: 
                        if np.size(bag_16) < bag_16_len: bag_16.append(val)
                    if zj == 6: 
                        if np.size(bag_66) < bag_66_len: bag_66.append(val)
                    if zj == 7: 
                        if np.size(bag_67) < bag_67_len: bag_67.append(val)
                    if zj == 8: 
                        if np.size(bag_68) < bag_68_len: bag_68.append(val)
                    if zj == 9: 
                        if np.size(bag_69) < bag_69_len: bag_69.append(val)

                if zi == 7:
                    if zj == 1: 
                        if np.size(bag_17) < bag_17_len: bag_17.append(val)
                    if zj == 6: 
                        if np.size(bag_67) < bag_67_len: bag_67.append(val)
                    if zj == 7: 
                        if np.size(bag_77) < bag_77_len: bag_77.append(val)
                    if zj == 8: 
                        if np.size(bag_78) < bag_78_len: bag_78.append(val)
                    if zj == 9: 
                        if np.size(bag_79) < bag_79_len: bag_79.append(val)

                if zi == 8: 
                    if zj == 1: 
                        if np.size(bag_18) < bag_18_len: bag_18.append(val)
                    if zj == 6: 
                        if np.size(bag_68) < bag_68_len: bag_68.append(val)
                    if zj == 7: 
                        if np.size(bag_78) < bag_78_len: bag_78.append(val)
                    if zj == 8: 
                        if np.size(bag_88) < bag_88_len: bag_88.append(val)
                    if zj == 9: 
                        if np.size(bag_89) < bag_89_len: bag_89.append(val)

                if zi == 9:
                    if zj == 1: 
                        if np.size(bag_19) < bag_19_len: bag_19.append(val)
                    if zj == 6: 
                        if np.size(bag_69) < bag_69_len: bag_69.append(val)
                    if zj == 7: 
                        if np.size(bag_79) < bag_79_len: bag_79.append(val)
                    if zj == 8: 
                        if np.size(bag_89) < bag_89_len: bag_89.append(val)
                    if zj == 9: 
                        if np.size(bag_99) < bag_99_len: bag_99.append(val)

        for _ in range(bag_11_len - np.size(bag_11)): bag_11.append(0)
        for _ in range(bag_66_len - np.size(bag_66)): bag_66.append(0)
        for _ in range(bag_77_len - np.size(bag_77)): bag_77.append(0)
        for _ in range(bag_88_len - np.size(bag_88)): bag_88.append(0)
        for _ in range(bag_99_len - np.size(bag_99)): bag_99.append(0)
        for _ in range(bag_16_len - np.size(bag_16)): bag_16.append(0)
        for _ in range(bag_17_len - np.size(bag_17)): bag_17.append(0)
        for _ in range(bag_18_len - np.size(bag_18)): bag_18.append(0)
        for _ in range(bag_19_len - np.size(bag_19)): bag_19.append(0)
        for _ in range(bag_67_len - np.size(bag_67)): bag_67.append(0)
        for _ in range(bag_68_len - np.size(bag_68)): bag_68.append(0)
        for _ in range(bag_69_len - np.size(bag_69)): bag_69.append(0)
        for _ in range(bag_78_len - np.size(bag_78)): bag_78.append(0)
        for _ in range(bag_79_len - np.size(bag_79)): bag_79.append(0)
        for _ in range(bag_89_len - np.size(bag_89)): bag_89.append(0)

        bag = (
            bag_11 + bag_66 + bag_77 + bag_88 + bag_99 + 
            bag_16 + bag_17 + bag_18 + bag_19 + bag_67 + 
            bag_68 + bag_69 + bag_78 + bag_79 + bag_89     
        )

        return bag 


    ''' 
        BoB(N) function:
    '''


    number = np.size(mol_Z)

    h_max = 16
    c_max = 7
    n_max = 6
    o_max = 4
    f_max = 5

    bag_11_len = h_max - 1  
    bag_66_len = c_max - 1   
    bag_77_len = n_max - 1   
    bag_88_len = o_max - 1    
    bag_99_len = f_max - 1 

    bag_16_len = np.max([h_max,c_max])
    bag_17_len = np.max([h_max,n_max]) 
    bag_18_len = np.max([h_max,o_max]) 
    bag_19_len = np.max([h_max,f_max]) 
    bag_67_len = np.max([c_max,n_max]) 
    bag_68_len = np.max([c_max,o_max]) 
    bag_69_len = np.max([c_max,f_max]) 
    bag_78_len = np.max([n_max,o_max]) 
    bag_79_len = np.max([n_max,f_max]) 
    bag_89_len = np.max([o_max,o_max]) 

    bag_len = (
        bag_11_len + bag_66_len + bag_77_len + bag_88_len + bag_99_len +  
        bag_16_len + bag_17_len + bag_18_len + bag_19_len + bag_67_len + 
        bag_68_len + bag_69_len + bag_78_len + bag_79_len + bag_89_len 
    )

    data = []

    for i in range(number):

        temp = []

        zatom = int(mol_Z[i])
        x,y,z = mol_R[i][0], mol_R[i][1], mol_R[i][2]

        temp.append(zatom)
        temp.append(float(x))
        temp.append(float(y))
        temp.append(float(z))

        data.append(temp)

    descriptor = []

    zero_bag = []
    for x in range(bag_len):
        zero_bag.append(0.0)

    for i in range(number):
        
        if mol_Z[i] == atomic_number(target_atom):

            index = find_index(number, data, i)
            neighbour = np.size(index)

            if bob_N == 0: 
                desc_bag = construct_bag(number,data,i,[]) # BoB0
            
            if bob_N == 1: 
                desc_bag = construct_bag(number,data,i,[]) + construct_bag(number,data,index[0],[i])  # BoB0+BoB1
            
            if bob_N == 2: 
                if neighbour >= 2: 
                    desc_bag = construct_bag(number,data,i,[]) + construct_bag(number,data,index[0],[i]) + construct_bag(number,data,index[1],[i])  # BoB0+BoB1+BoB2 
                elif neighbour == 1:
                    desc_bag = construct_bag(number,data,i,[]) + construct_bag(number,data,index[0],[i]) + zero_bag
            
            if bob_N == 3: 
                if neighbour >= 3: 
                    desc_bag = construct_bag(number,data,i,[]) + construct_bag(number,data,index[0],[i]) + construct_bag(number,data,index[1],[i]) + construct_bag(number,data,index[2],[i]) # BoB0+BoB1+BoB2+BoB3
                elif neighbour == 2:
                    desc_bag = construct_bag(number,data,i,[]) + construct_bag(number,data,index[0],[i]) + construct_bag(number,data,index[1],[i]) + zero_bag
                elif neighbour == 1:
                    desc_bag = construct_bag(number,data,i,[]) + construct_bag(number,data,index[0],[i]) + zero_bag            + zero_bag
                
            
            if bob_N == 4: 
                if neighbour >= 4: 
                    desc_bag = construct_bag(number,data,i,[]) + construct_bag(number,data,index[0],[i]) + construct_bag(number,data,index[1],[i]) + construct_bag(number,data,index[2],[i]) + construct_bag(number,data,index[3],[i])# BoB0+BoB1+BoB2+BoB3+BoB4
                elif neighbour == 3:
                    desc_bag = construct_bag(number,data,i,[]) + construct_bag(number,data,index[0],[i]) + construct_bag(number,data,index[1],[i]) + construct_bag(number,data,index[2],[i]) + zero_bag
                elif neighbour == 2:
                    desc_bag = construct_bag(number,data,i,[]) + construct_bag(number,data,index[0],[i]) + construct_bag(number,data,index[1],[i]) + zero_bag            + zero_bag
                elif neighbour == 1:
                    desc_bag = construct_bag(number,data,i,[]) + construct_bag(number,data,index[0],[i]) + zero_bag            + zero_bag            + zero_bag
                    
            
            descriptor.append(desc_bag)
    
    return descriptor


def descriptor_gen(target_atom,xyzfile,descriptor):

    z,r = readxyz(xyzfile)

    if descriptor == 'acm':  desc = acm(23,target_atom,z,r) # maximum_atom = 23
    if descriptor == 'bob0': desc = bob(0,target_atom,z,r) 
    if descriptor == 'bob1': desc = bob(1,target_atom,z,r)
    if descriptor == 'bob2': desc = bob(2,target_atom,z,r)
    if descriptor == 'bob3': desc = bob(3,target_atom,z,r)
    if descriptor == 'bob4': desc = bob(4,target_atom,z,r)

    return desc


#def main(xyz_file, target_atom, descriptor):
#
#    desc = descriptor_gen(target_atom, xyz_file, descriptor)
#    print(desc)


#if __name__ == "__main__":
#    if len(sys.argv) != 4:
#        print("Follow: python xyz_to_desc.py file.xyz 'target_atom' 'descriptor'")
#    else:
#        xyz_file = sys.argv[1]
#        target_atom = sys.argv[2]
#        descriptor = sys.argv[3]
#        main(xyz_file, target_atom, descriptor)

