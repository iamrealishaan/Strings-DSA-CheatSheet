def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome(s):
    n = len(s)  # Get the length of the input string `s`.
    longest = ""  # Initialize an empty string to store the longest palindrome found.

    # Outer loop: Iterate through each index `i` in the input string `s`.
    for i in range(n):
        # Inner loop: Iterate through each index `j` from `i` to the end of the string `s`.
        for j in range(i, n):
            # Extract the substring from index `i` to `j` (inclusive).
            substring = s[i:j+1]

            # Check if the substring is a palindrome using the `is_palindrome()` function.
            # If it is a palindrome and longer than the current `longest`,
            # update `longest` to store the new longest palindrome found.
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring

    return longest  # Return the longest palindrome found in the input string `s`.

# Example
input_str = "babad"
result = longest_palindrome(input_str)
print(result)  # Output: "bab"
