import numpy as np

from GF16 import GFT, sbox, sboxinv

def make_bin(n):
    n = bin(n)
    n = n.replace('0b', '')
    while(len(n) < 4):
        n = "0" + n
    n = list(n)
    n = [int(i) for i in n]
    return n
    
def RotNib(w):
    w = np.asarray(w)
    w = np.roll(w, 4)
    w = w.tolist()
    return w
    
def SubNib(w):
    a = []
    l = len(w)
    for i in range(0,l,4):
        n = w[i:i+4]
        n = ''.join(map(str,n))
        a = a + make_bin(sbox[int(n,2)])
    return a
    
def SubNib_inv(w):
    a = []
    l = len(w)
    for i in range(0,l,4):
        n = w[i:i+4]
        n = ''.join(map(str,n))
        a = a + make_bin(sboxinv[int(n,2)])
    return a
    
def ShRow(w):
    for i in range(4, 8):
        w[i], w[i+8] = w[i+8], w[i]
    return w
    
def XOR(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    c = np.logical_xor(a, b)
    c = c.astype(int)
    c = c.tolist()
    return c
    
def gen_S(x):
    s = []
    l = len(x)
    for i in range(0,l,4):
        n = x[i:i+4]
        n = ''.join(map(str,n))
        s.append(int(n,2))
    s = [[s[0], s[1]], [s[2], s[3]]]
    s = np.asarray(s)
    s = s.transpose()
    return s
    
def mat_mul(s):
    result = [[0,0], [0,0]]
    result[0][0] = GFT[s[0][0]][1] ^ GFT[s[0][1]][4]
    result[0][1] = GFT[s[0][0]][4] ^ GFT[s[0][1]][1]
    result[1][0] = GFT[s[1][0]][1] ^ GFT[s[1][1]][4]    
    result[1][1] = GFT[s[1][0]][4] ^ GFT[s[1][1]][1]
    result = sum(result,[])
    result = [make_bin(i) for i in result]
    result = sum(result, [])
    return result
    
def mat_mul_inv(s):
    result = [[0,0], [0,0]]
    result[0][0] = GFT[9][s[0][0]] ^ GFT[2][s[1][0]]
    result[0][1] = GFT[9][s[0][1]] ^ GFT[2][s[1][1]]
    result[1][0] = GFT[2][s[0][0]] ^ GFT[9][s[1][0]]    
    result[1][1] = GFT[2][s[0][1]] ^ GFT[9][s[1][1]]
    result = sum(result, [])
    result = [make_bin(i) for i in result]
    result = sum(result, [])
    return result
    
