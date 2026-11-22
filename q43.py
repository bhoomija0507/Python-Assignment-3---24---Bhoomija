nums = [10, 20, 30, 40, 50]
target = int(input("Enter element to find index of: "))

if target in nums:
    print("Index:", nums.index(target))
else:
    print("Element not found in list.")