def solution(n):
    answer = ''
    numbers = ['4', '1', '2']

    while n > 0:
        answer = numbers[n % 3] + answer
        n = (n - 1) // 3

    return answer