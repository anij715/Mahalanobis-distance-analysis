import pandas as pd
import numpy as np
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'breast-cancer-wisconsin.data')
data = pd.read_csv(my_file, header = None)
data.replace('?', np.nan, inplace = True)
data.dropna(axis='index', how='any', inplace = True)
#data.drop(data.columns[0,10], axis=1)
#data.columns = ["id number","Clump Thickness","Uniformity of Cell Size","Uniformity of Cell Shape","Marginal Adhesion","Single Epithelial Cell Size","Bare Nuclei","Bland Chromatin","Normal Nucleoli","Mitoses","Class"]
data.to_csv("HW1-win-data.csv", header = False)
