s = input("Enter a string: ")
digits = alphabets = special = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        alphabets += 1
    else:
        special += 1

print(f"Alphabets: {alphabets}, Digits: {digits}, Special Characters: {special}")