import os
import pandas as pd
import time

PATH = 'data/sources'

def tokenize(source_code):
    command = 'tokenizer -l C -t c {0}'.format(source_code)
    tokens = os.popen(command).read()
    return tokens

def load_train_data():
    start_time = time.process_time()
    train_data = pd.read_csv('data/train.csv', header= None, skiprows=1, encoding= 'utf-8-sig')
    train_data.columns = ['id_a', 'id_b', 'similarity']
    print(time.process_time() - start_time, "seconds")
    print("-----finished loading training data-----")
    return train_data

train_data = load_train_data()

def preprocess_input(train_data):
    all_tokens_list = []
    start_time = time.process_time()
    left_sources = train_data['id_a']
    left_sources_tokens = []
    for left_source in left_sources:
        left_tokens = []
        left_files = PATH + '/' + left_source
        left_tokens = tokenize(left_files)
        tokens_list = left_tokens.split("\n")
        all_tokens_list.append(tokens_list)
    print(all_tokens_list)
    print(len(all_tokens_list[1]))

preprocess_input(train_data)