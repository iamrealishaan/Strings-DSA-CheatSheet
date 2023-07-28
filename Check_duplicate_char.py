def duplicate_char(s):
    char_count = {}
    duplicates = []

    for char in s:
        if char in char_count:
            char_count[char] += 1  # Use '+=' to increment the count.
        else:
            char_count[char] = 1   # Use '=' to set the initial count to 1.

    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)

    return duplicates

input_str = "HELLO, World"
result = duplicate_char(input_str)
print(result)
