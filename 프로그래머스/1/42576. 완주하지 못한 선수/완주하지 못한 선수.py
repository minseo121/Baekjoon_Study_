def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    l = len(completion)
    for i in range(l):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

    