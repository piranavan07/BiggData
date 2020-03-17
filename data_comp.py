import pandas as pd
import numpy as np

data1 = pd.read_csv('C://Users//pirana//PycharmProjects//DataCompare//employees.csv')
data2 = pd.read_csv('C://Users//pirana//PycharmProjects//DataCompare//employees_copy.csv')
# print('''
# ======Data set 1 ======''')
# print(data1.describe())
# print('''
# ======Data set 2 ======''')
# print(data2.describe())
print('''
======Data set 1 & 2 salary match ======''')
data2['Salary match?'] = np.where(data1['Salary'] == data2['Salary'], 'True', 'False')
data2.to_csv('C://Users//pirana//PycharmProjects//DataCompare//out.csv')
print(data2)


