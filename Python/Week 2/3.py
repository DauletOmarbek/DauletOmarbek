def numIdenticalPairs(nums):
    a=int(0)
    for x in range(len(nums)-1):
        for y in range(x+1,len(nums)):
            if str(nums[x])==str(nums[y]):
                a+=1
    return a



nums=input().split()
print(numIdenticalPairs(nums))

