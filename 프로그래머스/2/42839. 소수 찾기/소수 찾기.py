def solution(numbers):
    num_set = set()

    def make(current, remain):
        if current != "":
            num_set.add(int(current))
        for i in range(len(remain)):
            make(current + remain[i], remain[:i] + remain[i+1:])

    make("", numbers)

    count = 0
    for n in num_set:
        if is_prime(n):
            count += 1
    return count


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True