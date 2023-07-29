#Check if the given string is shuffled substring of another string

def check_substring(str1,str2):
    sorted_s1 = ''.join(sorted(str1))
    sorted_s2 = ''.join(sorted(str2))
    return sorted_s1 in sorted_s2
s1 = " ishaan"
s2 = " shinaa"
result = check_substring(s1,s2)
print(result)
