nums = [3,4,2,2,1,3,3]

ok =[]
for each in nums:
    if nums.count(each) > 1 and each not in ok:
        ok.append(each)

print(ok)
