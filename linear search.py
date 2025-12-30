def linear_search(arr, target):
    for i in range(len(arr)): 
        if arr[i] == target: 
            return i 
    return -1  
arr = list(map(int, input("Enter the list of numbers separated by commas: ").split(',')))
target = int(input("Enter the target number: "))  
result = linear_search(arr, target)
if result != -1:
    print(f"Target found at index: {result}")
else:
    print("Target not found")
