# RC4-Attack

## Overview
This repository aims to implement the stream cipher algorithm RC4,
which was used in TLS protocol until 2015.
The weakness comes from its two core algorithm:
key scheduling algorithm (KSA) and pseudo-random generation algorithm (RSA),
which are implemented in `rc4.py`. This file is also used as my library for the
two files below.

## `WEPOutput.py`
Given a string that contains numbers or letter A-F, this file generates all
possible 24-bit initialization vector along with the first keyStreamByte and put
the reasult in `WEPOutputSim.csv`. The reason we assume that the first
keyStreamByte is available to the eavesdropper is that the first byte plain text
in WEP is always 'aa', which is from SNAP header. The eavesdropper can XOR 'aa'
with the first encrypted cipher to recover the first byte of key stream.

## `keyRecover.py`
This file reads in `WEPOutputSim.csv` and recover the original entered key. It
could be wrong but in most situation the result is always correct.

## Usage
First, use `WEPOutput.py` to generate simulated WEP packets. For example,
in terminal we put:
```
$ python WEPOutput.py AF1423
```
It will output in terminal:
```
WEPOutputSim.csv is generated sucessfully.
```
and also create a file name `WEPOutputSim.csv` to store the packets.
Then, use `keyRecover.py` to analyze this packet files by:
```
$ python keyRecover.py
```
It will output in terminal:
```
keyLength is: 3
AF1423
```

## Reference
https://link.springer.com/content/pdf/10.1007%2F3-540-45537-X_1.pdf

https://rickwash.com/papers/stream.pdf

https://en.wikipedia.org/wiki/RC4
