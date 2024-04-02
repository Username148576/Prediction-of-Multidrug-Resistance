import pandas as pd
import csv


test = pd.read_csv("./data/test_A_baumannii_mdr.csv")
train = pd.read_csv("./data/train_A_baumannii_mdr.csv")

with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i for i in range(0, 900)])

for i,k in zip(test['mz'],test['Intens']):
    now = 0
    max_row = 0
    max_seq = 0
    test_f = [0 for t in range(0, 900)]
    tmp = i.split(";")
    tmp1 = k.split(";")
    for j,r in zip(tmp,tmp1):
        if float(j)>2020+20*now:
            test_f[now] = max_seq
            max_seq = 0
            now += 1
        while float(j)>2020+20*now:
            now += 1
        if int(r) > 100:
            max_seq = max(max_seq, int(r))
            max_row = max(max_row, int(r))
    test_f[now] = max_seq
    if max_row != 0:
        test_f = [i/max_row for i in test_f]
    with open('test.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(test_f)

with open('train.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i for i in range(0, 900)])

for i,k in zip(train['mz'],train['Intens']):
    now = 0
    max_row = 0
    max_seq = 0
    train_f = [0 for t in range(0, 900)]
    tmp = i.split(";")
    tmp1 = k.split(";")
    for j,r in zip(tmp,tmp1):
        if float(j)>2020+20*now:
            train_f[now] = max_seq
            max_seq = 0
            now += 1
        while float(j)>2020+20*now:
            now += 1
        if int(r) > 100:
            max_seq = max(max_seq, int(r))
            max_row = max(max_row, int(r))
    train_f[now] = max_seq
    if max_row != 0:
        train_f = [i/max_row for i in train_f]
    with open('train.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(train_f)