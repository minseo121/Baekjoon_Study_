def solution(sequence):
    pulse1 = []
    pulse2 = []

    for i, num in enumerate(sequence):
        if i % 2 == 0:
            pulse1.append(num)
            pulse2.append(-num)
        else:
            pulse1.append(-num)
            pulse2.append(num)

    def max_array(arr):
        current = arr[0]
        result = arr[0]

        for num in arr[1:]:
            current = max(num, current + num)
            result = max(result, current)

        return result

    return max(max_array(pulse1), max_array(pulse2))