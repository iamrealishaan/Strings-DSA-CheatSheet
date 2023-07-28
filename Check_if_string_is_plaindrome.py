def check_palindrome(str1):
    if len(str1)<2:
        return str
    else:
        for i in range(len(str1)//2):
            if str1[i] == str1[len(str1)-i-1]:
                return True
        return False
while True:
    input_str = input("Enter Your string that you want to check and type exit if you want to quit : ", )
    if input_str.lower() == 'exit':
        break
    result = check_palindrome(input_str)
    if result:
        print("Yes its a palindrome")
    else:
        print("Not a palindrome")

