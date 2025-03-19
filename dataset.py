# from datasets import load_dataset

# ds = load_dataset("priyank-m/MJSynth_text_recognition")

# print(ds)

# import requests
# headers = {"Authorization": f"Bearer {API_TOKEN}"}
# API_URL = "https://datasets-server.huggingface.co/parquet?dataset=ibm/duorc"
# def query():
#     response = requests.get(API_URL, headers=headers)
#     return response.json()
# data = query()

# print(data)

# import requests
# headers = {"Authorization": f"Bearer {API_TOKEN}"}
# API_URL = "https://huggingface.co/api/datasets/ibm/duorc/parquet"
# def query():
#     response = requests.get(API_URL, headers=headers)
#     return response.json()
# urls = query()

# remove a file with extension .box into dataset

import os

dir_name = "/Users/bhavik/Downloads/archive 2/Template1/training_data/"
test = os.listdir(dir_name)

for item in test:
    print(item)
    if item.endswith(".box"):
        os.remove(os.path.join(dir_name, item))
for j in test :
    print(j)