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
 - Additionally, if you want to convert a SMILES string to an SVG image as in [query10.ipynb](https://github.com/moldis-group/pymoldis/blob/main/tutorial_ipynb/query_10.ipynb), install `rdkit`

- Download and install the package
```
    git clone git@github.com:moldis-group/pymoldis.git
    pip3 install -e pymoldis
```

- Install from PyPI
```
   pip3 install pymoldis==1.0.1
```

# Tutorial

The tutorial Jupiter notebooks are here: [tutorial_ipynb](https://github.com/moldis-group/pymoldis/tree/main/tutorial_ipynb)

Or, if you want to try a simple  query, try the following

```
   import pymoldis

   df=pymoldis.get_data('bigqm7w_S1T1')
   df.describe()
```

# References
[Ref-1] [_Resilience of Hund's rule in the Chemical Space of Small Organic Molecules_](https://arxiv.org/abs/2402.13801)    
Atreyee Majumdar, Raghunathan Ramakrishnan   
https://arxiv.org/abs/2402.13801 (2024)

[Ref-2][_The Resolution-vs.-Accuracy Dilemma in Machine Learning Modeling of Electronic Excitation Spectra_](https://doi.org/10.1039/D1DD00031D)                  
Prakriti Kayastha, Sabyasachi Chakraborty, Raghunathan Ramakrishnan    
Digital Discovery, 1 (2022) 689-702.    
