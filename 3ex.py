import os 
files = {}
for name in os.listdir("sorted"):
    with open(os.path.join("sorted", name), 'r', encoding='utf-8') as file:
        text = file.readlines()
        files[name] = len(text)

files_sorted = {}
sorted_keys = sorted(files, key=files.get)

for w in sorted_keys:
     files_sorted[w] = files[w]

for file_name, strings in files_sorted.items():
    print(file_name)
    with open (os.path.join("sorted", file_name), 'r', encoding='utf-8') as f:
        print(files_sorted[file_name])
        text = f.read()
        print(text)