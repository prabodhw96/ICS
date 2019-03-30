import numpy as np

def P10(arr):
    p10arr = []
    p10arr.append(arr[2])
    p10arr.append(arr[4])
    p10arr.append(arr[1])
    p10arr.append(arr[6])
    p10arr.append(arr[3])
    p10arr.append(arr[9])
    p10arr.append(arr[0])
    p10arr.append(arr[8])
    p10arr.append(arr[7])
    p10arr.append(arr[5])
    return p10arr
    
def P8(arr):
    p8arr = []
    p8arr.append(arr[5])
    p8arr.append(arr[2])
    p8arr.append(arr[6])
    p8arr.append(arr[3])
    p8arr.append(arr[7])
    p8arr.append(arr[4])
    p8arr.append(arr[9])
    p8arr.append(arr[8])
    return p8arr
    
def P4(arr):
    p4arr = []
    p4arr.append(arr[1])
    p4arr.append(arr[3])
    p4arr.append(arr[2])
    p4arr.append(arr[0])
    return p4arr
    
def IP(arr):
    iparr = []
    iparr.append(arr[1])
    iparr.append(arr[5])
    iparr.append(arr[2])
    iparr.append(arr[0])
    iparr.append(arr[3])
    iparr.append(arr[7])
    iparr.append(arr[4])
    iparr.append(arr[6])
    return iparr
    
def IP_inv(arr):
    ipiarr = []
    ipiarr.append(arr[3])
    ipiarr.append(arr[0])
    ipiarr.append(arr[2])
    ipiarr.append(arr[4])
    ipiarr.append(arr[6])
    ipiarr.append(arr[1])
    ipiarr.append(arr[7])
    ipiarr.append(arr[5])
    return ipiarr
    
def EP(arr):
    eparr = []
    eparr.append(arr[3])
    eparr.append(arr[0])
    eparr.append(arr[1])
    eparr.append(arr[2])
    eparr.append(arr[1])
    eparr.append(arr[2])
    eparr.append(arr[3])
    eparr.append(arr[0])
    return eparr
    
S0 = [["01", "00", "11","10"],
      ["11", "10", "01", "00"],
      ["00", "10", "01", "11"],
      ["11", "01", "11", "10"]]

def S0_val(arr):
    r = str(arr[0]) + str(arr[3])
    r = int(r, 2)
    c = str(arr[1]) + str(arr[2])
    c = int(c, 2)
    val = S0[r][c]
    return val
    
S1 = [["00", "01", "10", "11"],
      ["10", "00", "01", "11"],
      ["11", "00", "01", "00"],
      ["10", "01", "00", "11"]]

def S1_val(arr):
    r = str(arr[0]) + str(arr[3])
    r = int(r, 2)
    c = str(arr[1]) + str(arr[2])
    c = int(c, 2)
    val = S1[r][c]
    return val
    
def S_arr(string):
    s = []
    for i in range(0, len(string)):
        s.append(int(string[i]))
    return s
    
def LS1(arr):
    arr = np.asarray(arr)
    arr = np.roll(arr, -1)
    arr = arr.tolist()
    return arr
    
def LS2(arr):
    arr = np.asarray(arr)
    arr = np.roll(arr, -2)
    arr = arr.tolist()
    return arr
    
def split_arr(arr):
    n = int(len(arr)/2)
    x1 = arr[:n]
    x2 = arr[n:]
    return x1, x2
    
def XOR(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    c = np.logical_xor(a, b)
    c = c.astype(int)
    c = c.tolist()
    return c
    
