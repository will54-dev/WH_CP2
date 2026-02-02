# WH 2md notes reading files

import csv

file_path = "notes/read.txt"
csv_path = "notes\sample.csv"
try:
    with open(file_path, "w") as file:
        for item in range(5):
            file.write(f"{item+1}, me\n")
    with open(file_path, "r") as file:
        content = list()
        for line in file:
            content.append(line.strip())
except:
    print("no file")
else:
    for line in content:
        print(line)

try:
    with open(csv_path, mode= "r") as sample:
        reader = csv.reader(sample)
        header = next(reader)
        users = []
        for line in reader:
            users.append(
                {
                    header[0]: line[0],
                    header[1]: line[1]
                }
            )
except:
    print("no file CSV")
else:
    for user in users:
        print(user)