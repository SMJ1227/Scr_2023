def reverse(number):
    return eval(str(number)[::-1])

def isPalindrome(number):
    rev_num = reverse(number)
    if number == rev_num:
        return True
    else:
        return False

number = eval(input())
if isPalindrome(number):
    print("대칭수입니다.")
else:
    print("대칭수가 아닙니다.")
