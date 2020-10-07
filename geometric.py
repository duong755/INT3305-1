import math


def prob(n: int, p: float) -> float:
    """
    Parameters:
    - n (int): số lần thực hiện phép thử
    - p (float): xác suất phép thử thành công

    Returns:
    - float: xác suất hình học
    """
    pr = p * (1 - p) ** (n - 1)
    return pr


def infoMeasure(n: int, p: float) -> float:
    """
    Parameters:
    - n (int): symbol
    - p (float): xác suất phép thử thành công

    Returns:
    - float: lượng tin
    """
    pr = prob(n, p)
    info = -math.log2(pr)
    return info


def sumProb(N: int, p: float) -> float:
    """
    Tổng vô hạn Pr(1) + Pr(2) + ... bằng 1
    Dãy a_{N} = Pr(1) + Pr(2) + ... + Pr(N) là một dãy dương, tăng và có giới hạn bằng 1
    Do đó khi N càng lớn thì a_{N} càng xấp xỉ 1. Như vậy hàm sumProb cho phép kiểm tra
    tổng xác suất của biến ngẫu nhiên hình học bằng 1.

    Chứng minh bằng toán học có trong file explanation.pdf

    Parameters:
    - N (int): số lần thực hiện phép thử
    - p (float): xác suất phép thử thành công

    Returns:
    - float: tổng xác suất
    """
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p)
    return sum


def approxEntropy(N: int, p: float) -> float:
    """
    Xét dãy H_{N} = (-Pr(1) log Pr(1)) + (-Pr(2) log Pr(2)) + ...
    H_{N} là một dãy dương, tăng và có giới hạn là entropy của biến ngẫu nhiên hình học.
    Do đó khi N càng lớn, hàm approxEntropy sẽ tiến đến entropy của biến ngẫu nhiên hình học.

    Chứng minh bằng toán học, biểu thức entropy có trong file explanation.pdf

    Parameters:
    - N (int): số lần thực hiện phép thử
    - p (float): xác suất phép thử thành công

    Returns:
    - float: xấp xỉ entropy
    """
    entropy = 0
    for i in range(1, N + 1):
        entropy += prob(i, p) * infoMeasure(i, p)
    return entropy

print(approxEntropy(1000, 0.5)) # approximate 2