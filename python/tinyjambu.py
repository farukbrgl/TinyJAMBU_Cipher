#!/usr/bin/env python
# coding: utf-8
import tinyjambu_perm as perm
"""
TinyJAMBU Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye
https://csrc.nist.gov/CSRC/media/Projects/lightweight-cryptography/documents/finalist-round/updated-spec-doc/tinyjambu-spec-final.pdf
adresinden ulaşabilirsiniz.
"""


klen = 128
S = [0x0]*128
K = [0x0]*128
N = [0x0]*96
T = [0x0]*64
FB_n = [0,0,1]
FB_ad= [0,1,1]
FB_pc= [1,0,1]
FB_f = [1,1,1]

## The initialization
# Key setup
S = perm.state_update(S, K, 1024)

# Nonce setup
for i in range (2):
    a = 0
    b = 0
    S[36:38] = list(a ^ b for a, b in zip(S[36:38], FB_n))
    S = perm.state_update(S, K, 640)
    S[96:127] = list(a ^ b for a, b in zip(S[96:127], N[32*i:32*i+31]))


## Processing the associated data

print(S)