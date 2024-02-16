"""link to problem: https://codegolf.stackexchange.com/questions/270086/spot-the-difference"""

import random
a = [['@' if random.randint(1, 100) % 2 else ' ' for _ in range(16)] for _ in range(16)]
b = [['@' if random.randint(1, 100) % 2 else ' ' for _ in range(16)] for _ in range(16)]
s = sum([1 if a[i][j] != b[i][j] else 0 for i in range(16) for j in range(16)])
print(a)
print(b)
print(s)




