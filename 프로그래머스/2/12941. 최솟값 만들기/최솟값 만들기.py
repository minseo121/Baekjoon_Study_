def solution(A,B):
    n = len(A)
    result = 0
    A.sort()
    B.sort(reverse=True)
    for _ in range(n):
        result += A[-1]*B[-1]
        A.pop()
        B.pop()
    return result