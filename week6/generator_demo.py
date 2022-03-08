import pandas as pd

file_path = "./unisex_navne.xls"

df = pd.read_excel(file_path, header=None)
read_names_comp = (name for name in df.iloc[:,0])

print(next(read_names_comp))
print(next(read_names_comp))

# for n in read_names_comp:
#     print(n)


def read_names_def(names):
    i = 0
    while i < len(names):
        yield names[i]
        i += 1

read_def = read_names_def(df.iloc[:,0])
print(next(read_def))
print(next(read_def))

def read_names_from(names):
    yield from names

read_from = read_names_from(df.iloc[:,0])
print(next(read_from))
print(next(read_from))
