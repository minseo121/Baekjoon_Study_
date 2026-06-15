def to_min(t):
    return (t // 100) * 60 + (t % 100)

def solution(schedules, timelogs, startday):
    cnt = 0
    result = len(schedules)
    
    for i in range(len(schedules)):
        time = schedules[i]
        id = startday
        for j in timelogs[i]:
            if id == 7:
                id = 1
            elif id == 6:
                id+=1
            else:
                if to_min(j) - to_min(time) > 10:
                    cnt += 1
                    break
                else:
                    id += 1
    
    return result-cnt
        
                