# Program to Find wheather a character is Vowel or consonent

def vOrC(chr):
    if chr.lower() in 'aeiou':
        return f"{chr} is a Vowel"
    else:
        return f"{chr} is a Consonent"

if __name__=='__main__':
    print(vOrC(input("Enter a Character ")))

# Enter a Character E
# E is a Vowel