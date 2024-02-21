from setuptools import setup, find_packages

setup(
    name='pymoldis',
    version='1.0.1',
    packages=find_packages(),
    package_data={'pymoldis': ['data/*']},
    author='Raghunathan Ramakrishnan'
    author_email='raghu.rama.chem@gmail.com'
    include_package_data=True,
    url='https://github.com/raghurama123/qmlspectrum'
    license='MIT License'
    description='A Python suite for data-mining the Quantum Chemistry Big Data developed through the MolDis project (https://moldis.tifrh.res.in/)'
    long_desc_type="text/markdown"
    install_requires=[ 'pandas', 'numpy' ]
    include_package_data=True,
)


