#to check if one string is the rotation of another
def check_rotation(str1,str2):
    if len(str1) != len(str2):
        return False
    temp = str1 + str2
    return str2 in temp
input1 = 'abc'
input2 = 'cba'
result = check_rotation(input1,input2)
print(result)
