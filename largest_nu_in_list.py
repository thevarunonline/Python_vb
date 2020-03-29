nums=[1,3,4,5,21,8,9,20,7]
tmp=nums[0]
for i in nums:
    if tmp<i:
        tmp=i
print(tmp)
