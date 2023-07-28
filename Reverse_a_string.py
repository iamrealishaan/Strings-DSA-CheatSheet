def reverse_string(s1):
    if len(s1)<2:
        return s1
    else:
        return s1[::-1]

input_string = "Hi My Name Is Ishaan"
output_string = reverse_string(input_string)
print(output_string)
