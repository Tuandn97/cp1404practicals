for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

n = int(input("Enter the number of stars:"))
for i in range(n):
    print("*", end='')
print()

n = int(input("Enter the number of stars:"))
for i in range(n):
    for r in range(0, i+1):
        print("*", end='')
    print()



