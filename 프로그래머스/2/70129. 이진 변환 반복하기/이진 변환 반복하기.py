def solution(s):
    count = 0
    removed_zero = 0

    while s != '1':
        removed_zero += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        count += 1

    return [count, removed_zero]