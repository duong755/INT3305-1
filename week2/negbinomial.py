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
    """
    tính đúng đắn của công thức này được chứng minh bằng tổng xác suất trong file explanation.pdf
    """
    coefficient = binom(n - 1, r - 1) * 1.0
    q = 1 - p
    return coefficient * p ** r * q ** (n - r)


def infoMeasure(n: int, p: float, r: int) -> float:
    pr = prob(n, p, r)
    info = -math.log2(pr)
    return info


def sumProb(N: int, p: float, r: int) -> float:
    """
    Tổng Pr(1) + Pr(2) + ... bằng 1.
    Dãy c_{N} = Pr(1) + Pr(2) + ... + Pr(N) là một dãy dương, tăng và có giới hạn bằng 1.
    Do đó khi N càng lớn thì a_{N} càng xấp xỉ 1. Như vậy hàm sumProb cho phép kiểm tra
    tổng xác suất của biến ngẫu nhiên nhị thức âm bằng 1.
    ___
    Chứng minh bằng toán học có trong file explanation.pdf
    """
    sum = 0
    for i in range(r, N + 1):
        sum += prob(i, p, r)
    return sum


def approxEntropy(N: int, p: float, r: int) -> float:
    """
    Xét dãy H_{N} = (-Pr(1) log Pr(1)) + (-Pr(2) log Pr(2)) + ...
    H_{N} là một dãy dương, tăng và có giới hạn là entropy của biến ngẫu nhiên nhị thức âm
    Do đó khi N càng lớn, hàm approxEntropy sẽ tiến đến entropy của biến ngẫu nhiên nhị thức âm và hàm này có thể dùng để tính xấp xỉ entropy
    """
    entropy = 0
    for i in range(r, N + 1):
        entropy += prob(i, p, r) * infoMeasure(i, p, r)
    return entropy

print(sumProb(1000, 0.5, 4))
