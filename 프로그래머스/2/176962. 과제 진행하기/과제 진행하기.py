def moresub(subject, left, free_time, result, more):
    if left <= free_time:
        result.append(subject)
        remain = free_time - left
        if more and remain > 0:
            l = more.pop()
            moresub(l[0], l[1], remain, result, more)
    else:
        more.append([subject, left - free_time])


def solution(plans):
    result = []
    more = []
    for i in plans:
        t, m = i[1].split(':')
        i[1] = int(t) * 60 + int(m)
        i[2] = int(i[2])
    plans.sort(key=lambda x: x[1])

    for i in range(len(plans) - 1):
        free_time = plans[i + 1][1] - plans[i][1]
        moresub(plans[i][0], plans[i][2], free_time, result, more)

    result.append(plans[-1][0])
    while more:
        result.append(more.pop()[0])
    return result