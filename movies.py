# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:48:05 2015

@author: jonathan
"""

import pandas as pd
path = '/Users/jonathan/Desktop/Movie Project/'
movie = 'Movies1.csv'
movies = pd.read_table(movie, sep=',', header=0)
movies.columns
movie_cols = ['name', 'total_BO', 'domestic_BO', 'international_BO', 'domestic_DVD', 'production_budget']
movies.columns = movie_cols
pd.set_option('display.float_format', lambda x: '%.3f' % x)
movies.describe()
movies.head()
import matplotlib.pyplot as plt
movies.total_BO.plot(kind='hist')
movies.plot(kind='scatter', x='production_budget', y='total_BO', alpha=0.3)
movies_no_outliers = []
for p in movies:
    if 'total_BO'< 1000000000:
       movies_no_outliers.append(p) 

    
