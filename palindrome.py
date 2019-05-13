# WAP to identify if the no. is Palindrome or not
# Eg - 10801 == 10801

def palindrome(n):
    if str(n) == str(n)[::-1]:
        return f"{n} is a Palindrome"
    else:
        return f"{n} is Not a Palindrome"
    

if __name__ == '__main__':
    num = int(input("Enter a Number "))
    print(palindrome(num))

# Enter a Number 1001001
# 1001001 is a Palindrome