def solution(numbers, hand):
    result = []
    numM = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2),'*':(3,0), 0:(3,1), '#':(3,2)}
    li, ri = (3,0), (3,2)
    
    for i in numbers:
        if i == 1 or i ==4 or i == 7:
            li = numM[i]
            result.append("L")
        elif i == 3 or i == 6 or i == 9:
            ri = numM[i]
            result.append("R")
        else:
            target = numM[i]
            ld = abs(li[0]-target[0]) + abs(li[1]-target[1])
            rd = abs(ri[0]-target[0]) + abs(ri[1]-target[1])
            if ld < rd:
                result.append("L")
                li = numM[i]
            elif ld > rd:
                result.append("R")
                ri = numM[i]
            else:
                if hand == "right":
                    result.append("R")
                    ri = numM[i]
                else:
                    result.append("L")
                    li = numM[i]
    print(''.join(result))
    return ''.join(result)