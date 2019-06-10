import sys
from rc4 import *

possibleByte = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F' \
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if len(sys.argv) != 2:
    print("user input key (in hex) should be second argument")
    sys.exit()

rawkey = sys.argv[1]
if len(rawkey) % 2 != 0:
    print("key is not right, its length should be a multiple of 2")
    sys.exit()

for i in rawkey:
    if i not in possibleByte:
        print(rawkey)
        print(i)
        print(type(i))
        print("key should only contains 0-9 and A-F.")
        sys.exit()

key = []
i = 0
while i < len(rawkey):
    key.append(int(rawkey[i] + rawkey[i+1], 16))
    i += 2

# Initial IV form.
iv = [3, 255, 0]
sessionKey = iv + key
plainSNAP = "aa"

# Clear out what is originally in the file.
WEPOutputSim = open("WEPOutputSim.csv", "w").close()
# Append possible IV and keyStreamByte.
WEPOutputSim = open("WEPOutputSim.csv", "a")


# A is the number of known key bytes, it starts from 0 to the length of key.
for A in range(len(key)):
    iv[0] = A + 3
    for thirdByte in range(256):
        iv[2] = thirdByte
        sessionKey = iv + key
        box = []
        initSBox(box)
        ksaInt(sessionKey, box)

        i = 0
        j = 0
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        swapValueByIndex(box, i, j)
        keyStreamByte = box[(box[i] + box[j]) % 256]
        cipherByte = (int(plainSNAP, 16)) ^ keyStreamByte
        WEPOutputSim.write(str(iv[0]) + "," + str(iv[1]) + "," + str(iv[2]) + "," + str(cipherByte) + "\n")
print("WEPOutputSim.csv is generated sucessfully.")
