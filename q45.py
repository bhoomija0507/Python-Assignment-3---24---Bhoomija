items = [10, 20]

items.append(30)          # Adds single element at the end
items.extend([40, 50])    # Adds multiple elements from an iterable at the end
items.insert(1, 15)       # Inserts 15 at index 1

print("Final list:", items)