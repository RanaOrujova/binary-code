n = int(input("Enter a number that u wanna convert: "))
num = ""
basis=int(input("Enter the basis: "))
letter="0123456789ABCDEF"
while n > 0:
    k = n % basis
    n = n // basis
    num+=letter[k]

print(num[::-1])
