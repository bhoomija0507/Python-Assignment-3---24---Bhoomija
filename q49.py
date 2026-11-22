t = (10, 20, 30)

# Demonstrating immutability
try:
    t[0] = 99
except TypeError as e:
    print("Cannot modify tuple directly:", e)

# Creating a "modified" tuple via concatenation
modified_t = t[:1] + (25,) + t[2:]
print("Original tuple:", t)
print("New tuple via concatenation:", modified_t)