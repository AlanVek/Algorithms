import numpy as np
from math import log2


# Binary to decimal (int).
def bin2dec(num : np.array) -> int:
    return int(np.dot(num[::-1], 2 ** np.arange(len(num) + 0.0)).round())

# Binary IEEE 754 to decimal (float)
def binf2dec(num : np.array, ne : int) -> float:
    if ne >= len(num) - 1 or ne < 1: return 0
    if np.count_nonzero((num!=0) & (num!=1)): return 0

    signpart, expopart, mantpart = num[0], num[1 : ne + 1], num[ne + 1 :]
    sign, bias = (-1) ** signpart,  2 ** (ne - 1) - 1
    normal = 1

    one_count_exp = np.count_nonzero(expopart)
    all_zeros_exp, all_ones_exp = one_count_exp == 0, one_count_exp == len(expopart)
    all_zeros_mant = not np.count_nonzero(mantpart)

    if all_zeros_exp and all_zeros_mant: return 0
    elif all_zeros_exp and not all_zeros_mant: normal = 0
    elif all_ones_exp and all_zeros_mant: return np.inf * sign
    elif all_ones_exp and not all_zeros_mant: return np.nan

    expo = bin2dec(expopart) - bias + (1 - normal)
    mantisa = normal + bin2dec(mantpart) * 2.0 ** (-len(num) + ne + 1)
    return sign * 2.0 ** expo * mantisa



as_int = np.vectorize(int)

# Decimal (int) to binary.
def dec2bin(num: int, width: int = -1) -> np.array:
    if num <= 0: res = np.zeros(1, dtype = int)
    else:
        length = int(log2(num) + 1)
        expos = np.arange(length - 1, -1, -1)
        res = (num & as_int(2.0**expos)).astype(bool).astype(int)

    if res.size < width:
        res = np.concatenate((np.zeros(width - res.size, dtype = int), res))
    return res

def dec2binf_gen(num: float, ne: int, nm: int) -> np.array:

    if ne < 1 or nm < 1:
        return np.zeros(1 + nm + ne, dtype = int)

    BIAS = 2 ** (ne - 1) - 1

    # Nan
    if np.isnan(num):
        return np.concatenate(([0], np.ones(ne + nm, dtype = int)))

    abs_num, sign_bit = abs(num),  num < 0

    # Infinito o Cero
    if abs_num >= 2 ** (1 + BIAS):
        return np.concatenate(([sign_bit], np.ones(ne), np.zeros(nm))).astype(int)
    elif abs_num < 2 ** (1 - BIAS - nm):
        return np.concatenate(([sign_bit], np.zeros(ne + nm, dtype = int)))

    # Normal o Sub-Normal
    if abs_num >= 2**(1 - BIAS):
        exp = int(np.floor(log2(abs_num)))
        dec = abs_num / 2**exp - 1
    else:
        exp = -BIAS
        dec = abs_num / 2**(exp + 1)

    mantissa = dec2bin(int(2**nm * dec), nm)

    return np.concatenate(([sign_bit], dec2bin(exp + BIAS, ne), mantissa))

dec2binf = lambda num: dec2binf_gen(num, ne = 5, nm = 10)