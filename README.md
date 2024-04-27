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

If you want to try a simple  query, try the following

```
   import pymoldis

   df=pymoldis.get_data('bigqm7w_S1T1')
   df.describe()
```
which will return some statistics for the S1/T1 energies and the f01 oscillator strength calculated with TDDFT and ADC(2) methods.

To learn about more advanced queries, please go through the SI of our paper [https://arxiv.org/abs/2402.13801](https://arxiv.org/abs/2402.13801). The corresponding tutorial Jupyter notebooks are here: [tutorial_ipynb_bigqm7w_S1T1](https://github.com/moldis-group/pymoldis/tree/main/tutorial_ipynb_bigqm7w_S1T1)

# Specific References
### Singlet-Triplet energies of 13k molecules in the bigQM7w dataset

[_Resilience of Hund's rule in the Chemical Space of Small Organic Molecules_](https://arxiv.org/abs/2402.13801)    
Atreyee Majumdar, Raghunathan Ramakrishnan   
https://arxiv.org/abs/2402.13801 (2024)

___

### wB97XD/def2-TZVP dataset with 13k molecules upto 7 atoms of C/O/N/F

[_The Resolution-vs.-Accuracy Dilemma in Machine Learning Modeling of Electronic Excitation Spectra_](https://doi.org/10.1039/D1DD00031D)                  
Prakriti Kayastha, Sabyasachi Chakraborty, Raghunathan Ramakrishnan    
Digital Discovery, 1 (2022) 689-702.    

- bigQM7w dataset with DFT/TDDFT properties: [https://moldis-group.github.io/bigQM7w/](https://moldis-group.github.io/bigQM7w/)  

___

# Citing 

```
R Ramakrishnan (2024) "pymoldis: A Python suite for Molecular Discovery with Quantum Chemistry Big Data" https://github.com/moldis-group/pymoldis
```

## bibtex entry

```
@misc{ramakrishnan2024pymoldis,
  title   = {pymoldis: A Python suite for Molecular Discovery with Quantum Chemistry Big Data},
  author  = {Ramakrishnan, Raghunathan},
  url = {https://github.com/moldis-group/pymoldis},
  year    = {2024}
}
```

## Revision Notes
- _27 April 2024: For some molecules, we have updated the values of S1/T1 energies and the f01 oscillator strength at the SCS-PBE-QIDH/def2-TZVP levels. This revision was made because Orca 5.0.4 does not always print the excitation energies in ascending order. This however has very minimal effect on the overall statistics of the TDDFT results. We have recalculated TDDFT spectra with more eigenvalues and sorted to date to report the correct S1 and T1 energies. All other data are as the same as in our first release of the database on 15 February 2024._
