import urllib.request
#from bs4 import BeautifulSoup # parse html
import re #regex
import csv
import os
import json
import pandas as pd
import urllib.request
import joblib #load, dump pkl
from underthesea import word_tokenize #word_tokenize of lines
import numpy as np
import transformers as ppb # load model BERT
from transformers import BertModel, BertTokenizer
import torch
from sklearn.model_selection import train_test_split
# scrap comment = selenium
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from predict import list_data_comment
# import requests



def standardize_data(row):
    # remove stopword
    # Remove . ? , at index final
    row = re.sub(r"[\.,\?]+$-", "", row)
    # Remove all . , " ... in sentences
    row = row.replace(",", " ").replace(".", " ") \
        .replace(";", " ").replace("“", " ") \
        .replace(":", " ").replace("”", " ") \
        .replace('"', " ").replace("'", " ") \
        .replace("!", " ").replace("?", " ") \
        .replace("-", " ").replace("?", " ")
    
    row = row.lower()
    row = row.strip()
    return row

# Tokenizer
def tokenizer(row):
    return word_tokenize(row, format="text")

def analyze(result):
    good = np.count_nonzero(result)
    bad = len(result) - good
    print("số bình luận xấu = ", bad)
    print("số bình luận tốt = ", good)

    if good>bad:
        return "sản phẩm có nhiều bình luận tích cực, bạn có thể mua"
    else:
        return "sản phẩm có có nhiều bình luận tiêu cực, bạn nên xem xét trước khi mua"


def processing_data(list_data):
    # 1. Standardize data
    data_frame = pd.DataFrame(list_data, columns=['text'])
    print('data frame:', data_frame)
    data_frame['text'] = data_frame['text'].apply(standardize_data)

    # 2. Tokenizer
    data_frame['text'] = data_frame['text'].apply(tokenizer)

    # 3. Embedding
    X_val = data_frame['text']
    return X_val


def load_pretrainModel(data):
    
    '''
    Load pretrain model/ tokenizers
    Return : features
    '''
    model = BertModel.from_pretrained('bert-base-uncased')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    #encode lines
    tokenized = data.apply((lambda x: tokenizer.encode(x, add_special_tokens = True)))

    # get lenght max of tokenized
    max_len = 0
    for i in tokenized.values:
        if len(i) > max_len:
            max_len = len(i)
    print('max len:', max_len)

    # if lenght of tokenized not equal max_len , so padding value 0
    padded = np.array([i + [0]*(max_len-len(i)) for i in tokenized.values])
    print('padded:', padded[1])
    print('len padded:', padded.shape)

    #get attention mask ( 0: not has word, 1: has word)
    attention_mask = np.where(padded ==0, 0,1)
    print('attention mask:', attention_mask[1])

    # Convert input to tensor
    padded = torch.tensor(padded)
    attention_mask = torch.tensor(attention_mask)


    # Load model
    with torch.no_grad():
        last_hidden_states = model(padded, attention_mask =attention_mask)
    #     print('last hidden states:', last_hidden_states)

    features = last_hidden_states[0][:,0,:].numpy()
    print('features:', features)
    
    return features


def predict():
    # 1. Load URL and print comments
    link = "https://tiki.vn/serum-hoac-sua-rua-mat-giam-mun-mugung-7-ngay-hieu-qua-giam-mun-dau-den-mun-boc-lam-xep-khong-bong-da-acne-treatment-p171495459.html?spid=171495463&itm_campaign=tiki-reco_UNK_DT_UNK_UNK_deal-hot_UNK_rule-base-flash-deal-v3_UNK_RB_batched_PID.171495463&itm_medium=CPC&itm_source=tiki-reco&tclid=bd1204d7715039f0c095fe6ea7ca50a70be9619f704566fe9d7e1ddcbabfa713"
    data = list_data_comment(link)
    
    
    data_frame = processing_data(data)
    print(data_frame)
    features = load_pretrainModel(data_frame)
    # 2. Load weights
    model = joblib.load('save_model.pkl')
    # 3. Result
    result = model.predict(features)
    print(result)
    print(analyze(result))
# # predict(url ='https://tiki.vn/dien-thoai-samsung-galaxy-s20-plus-hang-chinh-hang-p48886153.html?src=search&2hi=0&keyword=s20&src=mega-menu')
# predict(url = 'https://www.lazada.vn/products/iphone-8-plus-chinh-hang-vna-moi-100-chua-kich-hoat-chua-qua-su-dung-bao-hanh-12-thang-tai-ttbh-apple-tra-gop-lai-suat-0-qua-the-tin-dung-man-hinh-retina-hd-55-inch-3d-touch-chip-a11-ios11-i757986604-s1985088475.html?spm=a2o4n.searchlistcategory.list.4.46d0bdd5OzWEVE&search=1')

predict()