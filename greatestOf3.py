# WAP to Find Greatest of 3 in a number

greatestOf3 = lambda x, y, z : x if x > y and x > z else y if y > z and y > x else z

if __name__ == '__main__':
    x = int(input("Enter num1 "))
    y = int(input("Enter num2 "))
    z = int(input("Enter num3 "))
    print(f"Greatest of {x}, {y}, {z} is {greatestOf3(x, y, z)}")

# Output
# Enter num1 1
# Enter num2 12
# Enter num3 10
# Greatest of 1, 12, 10 is 12