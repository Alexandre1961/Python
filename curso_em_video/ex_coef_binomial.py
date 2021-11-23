def fatorial(n):
    if n < 0:
        return 0
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


def fat(n):
    if n < 0:
        return 0
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f


def numero_binomial(n, k):
    return fatorial(n) / fatorial(k) * fatorial (n-k)


f = fatorial(-1)
print(f)

f = fat(5)
print(f)

res = numero_binomial(3, 1)
print(res)
