import os
import argparse
from datetime import datetime
from setuptools import find_packages, setup
from pkg_resources import resource_filename
import pandas as pd
import pymoldis

data_folder = resource_filename('pymoldis', 'data')

def get_data(dataset):

    logo, header = pymoldis.headers()
#   print(logo)
#   print(header)

    start_time = datetime.now()
    formatted_datetime = start_time.strftime("%Y-%m-%d %H:%M:%S")

#   print('')
#   print(' Current Time:', formatted_datetime)

    if dataset.lower() == 'bigqm7w_s1t1':

        df=pd.read_csv(os.path.join(data_folder, 'data_bigqm7w_S1T1.csv'))

#       parser = argparse.ArgumentParser(description='Options for pymoldis')

#       parser.add_argument('--summary', action='store_true', help='Print a summary of the dataset')
#   
#       args = parser.parse_args()
#   
#       if args.summary:
#           print('Data available:')
#           print('---------------')
#           columns=df.columns
#           for icol, col in enumerate(columns):
#               print(icol,col)
#           print('Summary of numerical data:')
#           print('--------------------------')
#           print(df.describe())
#           print('------------------')

    return df
