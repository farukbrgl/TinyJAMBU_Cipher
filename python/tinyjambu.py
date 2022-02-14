#!/usr/bin/env python
# coding: utf-8
import tinyjambu_perm as perm
"""
TinyJAMBU Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye
https://csrc.nist.gov/CSRC/media/Projects/lightweight-cryptography/documents/finalist-round/updated-spec-doc/tinyjambu-spec-final.pdf
adresinden ulaşabilirsiniz.
"""

## klen = 128
## other lengths and starting values are below
S = [0]*128
K = [0]*128
N = [0]*96
T = [0]*64
M = [0]*32
C = [0]*32
AD= [0]*32

FB_n = [0,0,1]
FB_ad= [0,1,1]
FB_pc= [1,0,1]
FB_f = [1,1,1]
def tinyjambu(S, K, N, T, M, C, AD, FB_n, FB_ad, FB_pc, FB_f):
    ## The initialization
    # Key setup
    S = perm.state_update(S, K, 1024)

    # Nonce setup
    for i in range (2):
        a = 0
        b = 0
        S[36:38] = list(a ^ b for a, b in zip(S[36:38], FB_n))
        S = perm.state_update(S, K, 640)
        a = 0
        b = 0
        S[96:127] = list(a ^ b for a, b in zip(S[96:127], N[32*i:32*i+31]))


    ## Processing the associated data
    for j in range (1):
        a = 0
        b = 0
        S[36:38] = list(a ^ b for a, b in zip(S[36:38], FB_ad))
        S = perm.state_update(S, K, 640)
        a = 0
        b = 0
        S[96:127] = list(a ^ b for a, b in zip(S[96:127], AD[32*j:32*j+31]))



    ## The encryption
    for k in range (1):
        a = 0
        b = 0
        S[36:38] = list(a ^ b for a, b in zip(S[36:38], FB_pc))
        S = perm.state_update(S, K, 1024)
        a = 0
        b = 0
        S[96:127] = list(a ^ b for a, b in zip(S[96:127], M[32*k:32*k+31]))
        a = 0
        b = 0
        C[32*k:32*k+31] = list(a ^ b for a, b in zip(S[64:95], M[32*k:32*k+31]))
        # print((C))
    # print(S)

    return C
a = tinyjambu(S, K, N, T, M, C, AD, FB_n, FB_ad, FB_pc, FB_f)
