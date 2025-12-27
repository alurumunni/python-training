def movezeroes(nums):
    x = [] 
    y = []  

    for i in nums:
        if i == 0:
            x.append(i)
        else:
            y.append(i)

    z = y + x
    return z


nums = [0, 1, 0, 3, 12]
result = movezeroes(nums)
print(result)
