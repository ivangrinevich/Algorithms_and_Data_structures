n, k = [int(i) for i in input().split()]
a = 1
b = 1
m = 1000000007
for i in range(n - k + 1, n + 1):
    b = (b * i) % m
for i in range(2, k + 1):
    a = (a * i) % m
result = 1
m_1 = m - 2
while m_1 != 0:
    if m_1 & 1:
        result = (result * a) % m
        m_1 -= 1
    else:
        a = (a * a) % m
        m_1 = m_1 // 2
print((result * b) % m)
