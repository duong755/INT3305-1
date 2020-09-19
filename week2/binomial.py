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


def prob(n: int, p: float, N: int) -> float:
    coefficient = binom(N, n) * 1.0
    q = 1 - p
    return coefficient * p ** n * q ** (N - n)


def infoMeasure(n: int, p: float, N: int) -> float:
    pr = prob(n, p, N)
    info = -math.log2(pr)
    return info


def sumProb(N: int, p: float) -> float:
    sum = 0.0
    for i in range(0, N + 1):
        sum += prob(i, p, N)
    return sum


def approxEntropy(N: int, p: float):
    entropy = 0
    for i in range(0, N + 1):
        entropy += prob(i, p, N) * infoMeasure(i, p, N)
    return entropy
