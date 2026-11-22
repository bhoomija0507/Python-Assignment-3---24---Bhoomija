original = [1, 2, 3]

# Direct assignment (creates a reference to the same list)
alias = original
alias.append(4)

# copy() (creates a shallow copy of the list)
copied = original.copy()
copied.append(5)

print("Original list (affected by alias):", original)
print("Direct assignment list:", alias)
print("Copied list (independent):", copied)