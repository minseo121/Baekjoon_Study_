def solution(seoul):
    num = seoul.index("Kim")
    result = []
    result.append("김서방은 ")
    result.append(num)
    result.append("에")
    result.append(" 있다")
    print(''.join(map(str, result)))
    return ''.join(map(str, result))