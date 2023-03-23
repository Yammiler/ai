import pandas as pd
import numpy as np


def write_data(data):

  df = pd.DataFrame(data, columns=get_key(data))
  # muốn hiển thị ra chữ trong csv thì chính lại thành utf16 nhưng khuyên ko nên vì ko cần thiết và nó khiến sai định dạng lưu(Không phải lỗi)
  df.to_csv("data.csv",encoding='utf8', index=False)
  d = pd.read_csv('data.csv')
  d.head()


def get_key(data):
  arr = []
  for i in data:
    arr.append(i)
  
  return arr
    
