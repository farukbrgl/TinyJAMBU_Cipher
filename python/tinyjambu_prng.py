# execution time : 410.777 s
import tinyjambu

S = [0] * 128
K = [0] * 128
N = [0] * 96
T = [0] * 64
M = [0] * 32
C = [0] * 32
AD = [0] * 32

FB_n = [0, 0, 1]
FB_ad = [0, 1, 1]
FB_pc = [1, 0, 1]
FB_f = [1, 1, 1]

f = open("random_numbers_tinyjambu.txt", "w")

for i in range(10000):
    M = tinyjambu.tinyjambu(S, K, N, T, M, C, AD, FB_n, FB_ad, FB_pc, FB_f)
    e = 0
    M_str = ''.join(str(e) for e in M)
    f.write(M_str + "\n")
    print(M_str)
