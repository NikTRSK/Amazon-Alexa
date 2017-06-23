import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import json
from pprint import pprint
from os import listdir
from os.path import isfile, join
import re
from itertools import filterfalse

def list_to_file(input_list, output_file):
    for item in input_list:
        output_file.write("%s\n" % item)

def remove_tags(input_array):
    for i in range(0, len(input_array)):
        res = re.search(r'<p>(.*)<', input_array[i])
        input_array[i] = res.group(1)
        if input_array[i].find("In ") is not -1:
            input_array[i] = input_array[i].replace("In ", "")

    return input_array

def remove_extra(input_array):
    extracted = filterfalse((lambda x: len(x) > 30), input_array)
    return extracted

def get_actor_list(data):
    with open('actors.txt', 'w') as actor_list:
        actors = data['title'].unique()
        list_to_file(actors, actor_list)        

def get_brand_list(data):
    with open('brands.txt', 'w') as brand_list:
        brands = data['description'].unique()
        brands = remove_tags(brands)
        brands = remove_extra(brands)
        list_to_file(brands, brand_list)

files = list(filter(lambda f: '.json' in f, listdir('.')))
data = pd.DataFrame()
for file in files:
    with open(file) as input_file:
        data = data.append (pd.read_json(input_file)[['description', 'url', 'title']]) # keep only the columns we need

data.to_csv('output.csv', index=False, encoding='utf-8')
get_actor_list(data)
get_brand_list(data)