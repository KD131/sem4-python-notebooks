import json
import pandas as pd

url = r"E:\Documents\Downloads\unique-artwork-20220415092417.json"

with open(url, 'r', encoding='utf-8') as f:
    lst = json.load(f)

df = pd.json_normalize(lst).filter(['name', 'colors', 'color_identity', 'image_uris.art_crop']) # can also slice or loc like [[]] or loc[:, []]
# print(df.head)
# print(df['image_uris.art_crop'])
# print(df[df['colors'] != df['color_identity']]) # no-cost cards have no color but have color_identity
df = df.drop('colors', axis=1) # drop unneeded colors column
df = df[df['color_identity'].apply(lambda x: len(x) == 1)] # trims out multi-colours, <=1 to include colourless
print(df[:20])
print(len(df))
