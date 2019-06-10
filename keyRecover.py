import sys, csv
from rc4 import *

ivFilename = "WEPOutputSim.csv"
rows = []
box = []
# In WEP, the header of SNAP is always 'aa'.
plainSNAP = "aa"

with open(ivFilename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

keyLength = int(rows[-1][0]) - 2
print("keyLength is: " + str(keyLength))

key = [None] * 3
for A in range(keyLength):
    prob = [0] * 256
    for row in rows:
        key[0] = int(row[0])
        key[1] = int(row[1])
        key[2] = int(row[2])

        j = 0
        initSBox(box)

        # Simulate the S-Box after KSA initialization.
        for i in range(A + 3):
            j = (j + box[i] + key[i]) % 256
            swapValueByIndex(box, i, j)
            # Record the original box[0] and box[1] value.
            if i == 1:
                original0 = box[0]
                original1 = box[1]

        i = A + 3
        z = box[1]
        # if resolved condition is possibly met.
        if z + box[z] == A + 3:
            # If the value of box[0] and box[1] has changed, discard this possibility.
            if (original0 != box[0] or original1 != box[1]):
                continue
            keyStreamByte = int(row[3]) ^ int(plainSNAP, 16)
            keyByte = (keyStreamByte - j - box[i]) % 256
            prob[keyByte] += 1
        # Assume that the most hit is the correct password.
        higherPossibility = prob.index(max(prob))
    key.append(higherPossibility)

# Get rid of first 24-bit initialization vector.
userInput = key[3:]
result = [format(key, 'x') for key in userInput]
rawkey = ''.join(result).upper()
print(rawkey)
