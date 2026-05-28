key = [0x13, 0x37, 0x42, 0x55]
encrypted = [
    95, 124, 17, 46, 112, 3, 33, 100, 125, 80,
    29, 54, 114, 84, 43, 100, 34, 80, 29, 59,
    114, 80, 35, 10, 125, 86, 37, 97, 110
]

flag = ''.join(chr(e ^ key[i % len(key)]) for i, e in enumerate(encrypted))
print(flag)
