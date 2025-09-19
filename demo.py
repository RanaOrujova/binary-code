n = int(input("Enter a number that u wanna convert: "))
num = []
basis=int(input("Enter the basis: "))
letter=''
while n > 0:
    k = n % 2 #If you want to convert a number to another base, write that base instead of 2.
    binary.append(k)
    n = n // 2 #also here
    if basis==16:
        k = n % basis
        n = n // basis
        if k>=10:
            if k==10:
                letter='A'
            if k==11:
                letter='B'
            if k==12:
                letter='C'
            if k==13:
                letter='D'
            if k==14:
                letter='E'
            if k==15:
                letter='F'
            num.append(letter)
        else:
            num.append(k)
    else:
        k = n % basis
        n = n // basis
        num.append(k)

print(binary[::-1])
print(num[::-1])
