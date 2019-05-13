# Wap to find number is Strong or not
"""Strong numbers are the numbers whose sum of factorial of digits is equal to the original number.
A strong number is such that the sum of it's factorial is the number itself, lets take example, 
A number 145 is strong because factorial of 1, 4, 5 is equals to 145."""

fact = lambda x: 1 if x == 0 else x * fact(x-1)

def strongNum(num):
    sum = 0
    for i in (str(num)):
        sum+=fact(int(i))
    return(sum == num)

if __name__ == '__main__':
    num = int(input("Enter a Number "))
    if strongNum(num):
        print(f"{num} is a Strong Number")
    else:
        print(f"{num} is NOT a Strong Number")