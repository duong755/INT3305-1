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
    """
    N >= n

    Parameters:
    - n (int): số lần phép thử thành công
    - p (float): xác suất phép thử thành công
    - N (int): số lần thực hiện phép thử

    Returns:
    - float: xác suất nhị thức
    """
    coefficient = binom(N, n) * 1.0
    q = 1 - p
    return coefficient * p ** n * q ** (N - n)


def infoMeasure(n: int, p: float, N: int) -> float:
    """
    Parameters:
    - n (int): số lần phép thử thành công
    - p (float): xác suất phép thử thành công
    - N (int): số lần thực hiện phép thử

    Returns:
    - float: lượng tin
    """
    pr = prob(n, p, N)
    info = -math.log2(pr)
    return info


def sumProb(N: int, p: float) -> float:
    """
    Biến ngẫu nhiên nhị thức chỉ có hữu hạn symbol, tổng xác suất của tất cả các symbol này bằng 1.
    Do đó hàm sumProb cho phép kiểm tra tổng xác suất của biến ngẫu nhiên nhị thức bằng 1.

    Chứng minh toán học có trong file explanation.pdf

    Parameters:
    - N (int): số lần thực hiện phép thử nhiều nhất
    - p (float): xác suất phép thử thành công

    Returns:
    - float: tổng xác suất
    """
    sum = 0.0
    for i in range(0, N + 1):
        sum += prob(i, p, N)
    return sum


def approxEntropy(N: int, p: float) -> float:
    """
    Các symbol của biến ngẫu nhiên nhị thức là hữu hạn, do đó entropy cũng hữu hạn (bị chặn trên)
    Khi N càng lớn thì approxEntropy(N, p) càng xấp xỉ với entropy nên hàm này cho phép tính xấp xỉ entropy.

    Parameters:
    - N (int): số lần thực hiện phép thử nhiều nhất
    - p (float): xác suất phép thử thành công

    Returns:
    - float: xấp xỉ entropy
    """
    entropy = 0
    for i in range(0, N + 1):
        entropy += prob(i, p, N) * infoMeasure(i, p, N)
    return entropy

print("approxEntropy(100, 0.5) =", approxEntropy(100, 0.5))
