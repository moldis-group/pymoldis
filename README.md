# `pymoldis` ✨

```
┏┓  ┳┳┓  ┓┳┓• 
┃┃┓┏┃┃┃┏┓┃┃┃┓┏
┣┛┗┫┛ ┗┗┛┗┻┛┗┛
   ┛                                                                                                         
```
 A Python suite for data-mining the Quantum Chemistry Big Data developed through the MolDis project (https://moldis.tifrh.res.in/)  
 Support e-mail: ramakrishnan@tifrh.res.in

# Install `pymoldis` 

 - Install dependencies `numpy`, `pandas`
 - Additionally, if you want to convert a SMILES string to an SVG image as in [query10.ipynb](https://github.com/moldis-group/pymoldis/blob/main/tutorial_ipynb_bigqm7w_S1T1/query_10.ipynb), install `rdkit`

- Download and install the package
```
    git clone git@github.com:moldis-group/pymoldis.git
    pip3 install -e pymoldis
```

- Install from PyPI
```
   pip3 install pymoldis
```

# Tutorial

## Data-mining S1-T1 energies of bigQM7w dataset

The tutorial Jupyter notebooks are here: [tutorial_ipynb_bigqm7w_S1T1](https://github.com/moldis-group/pymoldis/tree/main/tutorial_ipynb_bigqm7w_S1T1)

Or, if you want to try a simple  query, try the following

```
   import pymoldis

   df=pymoldis.get_data('bigqm7w_S1T1')
   df.describe()
```
# Citing QML

```
R Ramakrishnan (2024) "pymoldis: A Python suite for data-mining the Quantum Chemistry Big Data" https://github.com/moldis-group/pymoldis
```

## bibtex

```
@misc{ramakrishnan2024pymoldis,
  title   = {pymoldis: A Python suite for data-mining the Quantum Chemistry Big Data},
  author  = {Ramakrishnan, Raghunathan},
  url = {https://github.com/moldis-group/pymoldis},
  year    = {2024}
}
```

# Specific References
- Singlet-Triplet energies of 13k molecules in the bigQM7w dataset

[Ref-1] [_Resilience of Hund's rule in the Chemical Space of Small Organic Molecules_](https://arxiv.org/abs/2402.13801)    
Atreyee Majumdar, Raghunathan Ramakrishnan   
https://arxiv.org/abs/2402.13801 (2024)

- wB97XD/def2-TZVP minimum energy geometries of 13k molecules in the bigQM7w dataset with upto 7 atoms of C/O/N/F

[Ref-2][_The Resolution-vs.-Accuracy Dilemma in Machine Learning Modeling of Electronic Excitation Spectra_](https://doi.org/10.1039/D1DD00031D)                  
Prakriti Kayastha, Sabyasachi Chakraborty, Raghunathan Ramakrishnan    
Digital Discovery, 1 (2022) 689-702.    
