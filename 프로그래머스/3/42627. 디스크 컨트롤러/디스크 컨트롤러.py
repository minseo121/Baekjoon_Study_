def solution(jobs):
    jobs = sorted(jobs)
    n = len(jobs)
    current_time = 0
    idx = 0
    done = 0
    total = 0
    queue = []

    while done < n:
        while idx < n and jobs[idx][0] <= current_time:
            queue.append(jobs[idx])
            idx += 1

        if not queue:
            current_time = jobs[idx][0]
            continue

        queue.sort(key=lambda x: x[1])
        job = queue.pop(0)
        current_time += job[1]
        total += current_time - job[0]
        done += 1

    return total // n