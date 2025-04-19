a = int(input())

if a % 2 == 0:
    a = a - 1

num = 1
odd_numbers = []
for i in range(a):
    odd_numbers.append(str(num))
    num += 2

print(",".join(odd_numbers))
