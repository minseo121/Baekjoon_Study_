def solution(n, results):
    win = [[False]*(n+1) for _ in range(n+1)]
    for a, b in results:
        win[a][b] = True
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if win[i][k] and win[k][j]:
                    win[i][j] = True #k를 거쳐서 이길 수 있음 직접 이기는 것
                    #플로이드-워셜 알고리즘
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if i == j:
                continue
            if win[i][j] or win[j][i]:
                cnt += 1
        if cnt == n-1:
            answer += 1
    return answer