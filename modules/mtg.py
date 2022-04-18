from concurrent.futures import ThreadPoolExecutor
import json
import os
import pandas as pd
import requests

url = r"E:\Documents\Downloads\unique-artwork-20220415092417.json"

with open(url, 'r', encoding='utf-8') as f:
    lst = json.load(f)

df = pd.json_normalize(lst).filter(['id', 'name', 'color_identity', 'image_uris.art_crop']) # can also slice or loc like [[]] or loc[:, []]
# loc works with index if the df is indexed by index. You know?

# print(df.head)
# print(df['image_uris.art_crop'])
# print(df[df['colors'] != df['color_identity']]) # no-cost cards have no color but have color_identity
# df = df.drop('colors', axis=1) # drop unneeded colors column

# trims out multi-colours, <=1 to include colourless
df = df[df['color_identity'].apply(lambda x: len(x) == 1)]
# removes cards with no direct art_crop url, e.g. cards with more faces so the url is further down and more than one.
df = df[df['image_uris.art_crop'].notna()]
# print(df[:20])
# print(len(df))

# download first 2000 art images
df = df[:2000]
# why does [] work with int indexes. Not even index, it gives the correct size, 2000, despite indices missing.
# why can you sometimes mix int index or slice with column labels, and sometimes have to combine iloc and loc.
# I'm so confused.
print(df.head)

images_path = 'mtg_images'
os.makedirs(images_path, exist_ok=True)

def download(path, url):
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)

def download_from_row(row):
    row = row[1]
    path = 'mtg_images/{} {}.jpg'.format(row['color_identity'], row['id'])
    url = row['image_uris.art_crop']
    download(path, url)

def check_if_all_cards_downloaded():
    """Prints subset of cards in the dataset that are not present in image folder"""
    with os.scandir('mtg_images') as it:
        ids = [file.name.split(' ')[1].split('.')[0] for file in it]
        print(df[~df['id'].isin(ids)])

with ThreadPoolExecutor(5) as exec:
    exec.map(download_from_row, df.iterrows())
