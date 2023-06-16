import os 
files = {}
for name in os.listdir("sorted"):
    with open(os.path.join("sorted", name), 'r', encoding='utf-8') as file:
        text = file.readlines()
        files[name] = len(text)
files = sorted(files.items(), key = lambda x:x[1])

for file_name in files:
    with open ('1.txt', 'rt', encoding="utf-8") as file:
        print(file_name, sep = '\n')
        res = file.read()
        print(res)