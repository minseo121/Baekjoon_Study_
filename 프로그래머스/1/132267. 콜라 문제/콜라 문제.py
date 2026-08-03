def solution(a, b, n):
    result = 0
    while True:
        if n >= a:
            cola = b*(n//a)
            n = n % a
            n += cola
            result += cola
        else:
            break
    return result