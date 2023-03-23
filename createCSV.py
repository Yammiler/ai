import pandas as pd
import numpy as np


def write_data(data):

  df = pd.DataFrame(data, columns=get_key(data))
  df.to_csv("data.csv",encoding='utf8', index=False)
  d = pd.read_csv('data.csv')
  d.head()


def get_key(data):
  arr = []
  for i in data:
    arr.append(i)
  
  return arr
    