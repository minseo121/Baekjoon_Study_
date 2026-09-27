def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1
    start = 1

    for station in stations:
        end = station - w

        if start < end:
            gap = end - start
            answer += (gap + coverage - 1) // coverage

        start = station + w + 1

    if start <= n:
        gap = n - start + 1
        answer += (gap + coverage - 1) // coverage

    return answer