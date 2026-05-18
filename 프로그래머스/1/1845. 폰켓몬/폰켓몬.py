def solution(nums):
    dict = {}
    N = len(nums)
    for i in range(len(nums)):
        dict[nums[i]]=i
    l = len(dict)
    if l >= N//2:
        return N//2
    else:
        return l
    