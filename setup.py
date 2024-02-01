from setuptools import setup, find_packages

setup(
    name='pymoldis',
    version='0.1',
    packages=find_packages(),
    package_data={'pymoldis': ['data/*']},
    include_package_data=True,
    install_requires=[
    ],
)
