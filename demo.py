n = int(input())
binary = []

while n > 0:
    k = n % 2 #If you want to convert a number to another base, write that base instead of 2.
    binary.append(k)
    n = n // 2 #also here

print(binary[::-1])
