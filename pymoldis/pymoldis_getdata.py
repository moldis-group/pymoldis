import os
from setuptools import find_packages, setup
from pkg_resources import resource_filename
from datetime import datetime
import pandas as pd
import csv

data_folder = resource_filename('pymoldis', 'data')

def get_data():
    df=pd.read_csv(os.path.join(data_folder, 'data_bigqm7w.csv'))
    return df
