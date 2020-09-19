import math


def prob(n: int, p: float) -> float:
    pr = p * (1 - p) ** (n - 1)
    return pr


def infoMeasure(n: int, p: float) -> float:
    pr = prob(n, p)
    info = -math.log2(pr)
    return info


def sumProb(N: int, p: float) -> float:
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p)
    return sum


def approxEntropy(N: int, p: float) -> float:
    entropy = 0
    for i in range(1, N + 1):
        entropy += prob(i, p) * infoMeasure(i, p)
    return entropy

print(approxEntropy(1000, 0.5)) # approximate 2