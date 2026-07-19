def solution(numbers):
    result = []
    for x in numbers:
        if x % 2 == 0:#짝수
            result.append(x + 1)
        else:#홀수       
            cnt = 0
            temp = x
            while temp % 2 == 1:
                cnt += 1
                temp //= 2
            result.append(x + 2 ** (cnt - 1))
    return result