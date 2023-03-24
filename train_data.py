import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import torch
import transformers
from transformers import BertModel, BertTokenizer
import joblib


df = pd.read_csv('data.csv', delimiter='\t', header=None)
print(df.shape)
# get all rows
print(df[0])

# '''
# Load pretrain model/ tokenizers
# '''
# model = BertModel.from_pretrained('bert-base-uncased')
# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# #encode lines
# tokenized = df[0].apply((lambda x: tokenizer.encode(x, add_special_tokens = True)))
# print('encode',tokenized[1])
# # decode
# print('decode',tokenizer.decode(tokenized[1]))

# #get all label 
# labels = np.zeros(len(df[0]))
# for i in range(len(df[0])):
#     labels[i] = df[0][i][-1]
# print('labels shape:', labels.shape)

# # get lenght max of tokenized
# max_len = 0
# for i in tokenized.values:
#     if len(i) > max_len:
#         max_len = len(i)
# print('max len:', max_len)

# # if lenght of tokenized not equal max_len , so padding value 0
# padded = np.array([i + [0]*(max_len-len(i)) for i in tokenized.values])
# print('padded:', padded[1])
# print('len padded:', padded.shape)

# #get attention mask ( 0: not has word, 1: has word)
# attention_mask = np.where(padded ==0, 0,1)
# print('attention mask:', attention_mask[1])

# # Convert input to tensor
# padded = torch.tensor(padded)
# attention_mask = torch.tensor(attention_mask)


# # Train model
# with torch.no_grad():
#     last_hidden_states = model(padded, attention_mask =attention_mask)
# #     print('last hidden states:', last_hidden_states)

# features = last_hidden_states[0][:,0,:].numpy()
# print('features:', features)

# X_train, X_test, y_train, y_test = train_test_split(features, labels)

# cl = LogisticRegression()
# cl.fit(X_train, y_train)

# # Save model
# joblib.dump(cl, 'save_model.pkl')
# sc = cl.score(X_test, y_test)
# print('score:', sc)
