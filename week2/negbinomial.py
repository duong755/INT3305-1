import math


def binom(n: int, k: int) -> int:
    if 0 <= k <= n:
        if k == 0 or k == n:
            return 1
        else:
            result = 1.0
            for i in range(1, k + 1):
                result *= (n - k + i) * 1.0 / i * 1.0
            return int(result)
    else:
        return 0


def prob(n: int, p: float, r: int) -> float:
    coefficient = binom(n, n - r + 1)
    q = 1 - p
    return coefficient * p ** r * q ** (n - r + 1)


def infoMeasure(n: int, p: float, r: int) -> float:
    pr = prob(n, p, r)
    info = -math.log2(pr)
    return info


def sumProb(N: int, p: float, r: int) -> float:
    sum = 0
    for i in range(r, N + 1):
        sum += prob(i, p, r)
    return sum


def approxEntropy(N: int, p: float, r: int) -> float:
    entropy = 0
    for i in range(r, N + 1):
        entropy += prob(i, p, r) * infoMeasure(i, p, r)
    return entropy
