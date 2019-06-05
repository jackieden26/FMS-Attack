import sys, csv
from rc4 import *

ivFilename = "WEPOutputSim.csv"
rows = []
box = []
plainSNAP = "aa"

with open(ivFilename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

keyLength = int(rows[-1][0]) - 2
print("keyLength is: " + str(keyLength))

key = [None] * 3
for A in range(keyLength):
    prob = [None] * 256
    for i in range(256):
        prob[i] = 0

    for row in rows:

        key[0] = int(row[0])
        key[1] = int(row[1])
        key[2] = int(row[2])

        j = 0

        initSBox(box)

        for i in range(A + 3):
            j = (j + box[i] + key[i]) % 256
            swapValueByIndex(box, i, j)
