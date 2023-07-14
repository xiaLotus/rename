import os

folder = r'tinyjambu\\'
count = 1

for file_name in os.listdir(folder):
    source = folder + file_name

    des = folder + "R" + str(count) + "_tinyjambu.csv"

    os.rename(source, des)
    count += 1

res = os.listdir(folder)
print(res)