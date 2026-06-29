def solution(board, moves):
    result = []
    cnt = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                if result and result[-1] == board[j][i-1]:
                    result.pop()
                    cnt+=2
                else:
                    result.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return cnt