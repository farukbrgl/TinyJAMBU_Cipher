def state_update(S, K, i_round):
    for i in range (i_round):
        feedback = S[0] ^ S[47] ^ (0x1 - (S[70] & S[85])) ^ S[91] ^ (K[(i % klen)])
        for j in range(127):
            S.insert(0, S.pop())
            # print(S)
        S[127] = feedback
    return S

#128-bit key
#96-bit nonce
#64-bit tag
#128-bit state
klen = 128
S = [0x0]*128
K = [0x0]*128

a = state_update(S, K, 2048)
