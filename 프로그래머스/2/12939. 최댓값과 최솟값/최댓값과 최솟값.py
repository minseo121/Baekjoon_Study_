def solution(s):
    nums = list(map(int,s.split(" ")))
    nums.sort()
    return " ".join(map(str, [nums[0], nums[-1]]))