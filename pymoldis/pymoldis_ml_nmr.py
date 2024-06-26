import os
import pymoldis as pym
import numpy as np
import pandas as pd
from pkg_resources import resource_filename

def dij_sparse(N1, N2, ind1, ind2, x1, x2, lpnorm):

    N = np.max([np.max(ind1), np.max(ind2)])+1

    a1 = np.zeros(N)
    for i1 in range(N1):
        a1[ind1[i1]] = x1[i1]

    a2 = np.zeros(N)
    for i2 in range(N2):
        a2[ind2[i2]] = x2[i2]

    dij_sparse_value = np.sum(np.abs(a1 - a2)**lpnorm)

    return dij_sparse_value

def direct_ml(ele,rep,target,xyzfile):

    ZERO=1e-14

    data_folder = resource_filename('pymoldis', 'data')

    if ele == 'H' and rep == 'bob3' :
        sigma = 507.25372667
        lpnorm = 1
        descfile=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/H_uff_Bob3.dat')
        if target == 'CCSD(T)':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/H_model_direct_CCSDT.csv')
        elif target == 'CCSD':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/H_model_direct_CCSD.csv')
        elif target == 'MP2':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/H_model_direct_MP2.csv')

    elif ele == 'C' and rep == 'bob3' :
        sigma = 519.45058153
        lpnorm = 1
        descfile=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/C_uff_Bob3.dat')
        if target == 'CCSD(T)':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/C_model_direct_CCSDT.csv')
        elif target == 'CCSD':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/C_model_direct_CCSD.csv')
        elif target == 'MP2':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/C_model_direct_MP2.csv')

    elif ele == 'N' and rep == 'bob3' :
        sigma = 595.26753085
        lpnorm = 1
        descfile=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/N_uff_Bob3.dat')
        if target == 'CCSD(T)':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/N_model_direct_CCSDT.csv')
        elif target == 'CCSD':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/N_model_direct_CCSD.csv')
        elif target == 'MP2':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/N_model_direct_MP2.csv')
  
    elif ele == 'O' and rep == 'bob3' :
        sigma = 595.57853740
        lpnorm = 1
        descfile=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/O_uff_Bob3.dat')
        if target == 'CCSD(T)':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/O_model_direct_CCSDT.csv')
        elif target == 'CCSD':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/O_model_direct_CCSD.csv')
        elif target == 'MP2':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/O_model_direct_MP2.csv')
  
    elif ele == 'F' and rep == 'bob3' :
        sigma = 481.49789679
        lpnorm = 1
        descfile=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/F_uff_Bob3.dat')
        if target == 'CCSD(T)':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/F_model_direct_CCSDT.csv')
        elif target == 'CCSD':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/F_model_direct_CCSD.csv')
        elif target == 'MP2':
            model=os.path.join(data_folder, 'bigqm7w_nmr_ml_models/F_model_direct_MP2.csv')

    desc = pym.descriptor_gen(ele, xyzfile, rep)

    at_desc=desc[0]

    NNZ=0
    for i,idesc in enumerate(at_desc):
        if abs(idesc) > ZERO:
            NNZ=NNZ+1

    ind_CM=[]
    for i,idesc in enumerate(at_desc):
        if abs(idesc) > ZERO:
            ind_CM.append(i)
   
    CM=[]
    for idesc in at_desc:
        if abs(idesc) > ZERO:
            CM.append(idesc)


    df = pd.read_csv(model,header=None)

    coeff=np.array(df[0])


    with open(descfile, 'r') as file:
        lines = file.readlines()

    pred=0

    for i,line in enumerate(lines):
   
        line=line.split()
      
        NNZ_t=int(line[0])
      
        ind_CM_t=[]
        for t in range(NNZ_t):
            ind_CM_t.append(int(line[t+1]))
      
        CM_t=[]
        for t in range(NNZ_t):
            CM_t.append(float(line[t+NNZ_t+1]))
      
        dij=dij_sparse(NNZ, NNZ_t, ind_CM, ind_CM_t, CM, CM_t, lpnorm)
      
        pred=pred+coeff[i]*np.exp(-dij/sigma)


    with open(xyzfile, 'r') as file:
        lines = file.readlines()
   
    for iline, line in enumerate(lines):
        line=line.strip()
        if iline <= 1:
            print(line)
        else:
            qele=line[0]
            if qele == ele:
                print(line,pred)
            else:
                print(line)

    return pred


