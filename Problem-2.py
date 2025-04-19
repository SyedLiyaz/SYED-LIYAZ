a = int(input())

odd_numbers = []

num = 1
for i in range(a):
    odd_numbers.append(str(num))
    num += 2
print(",".join(odd_numbers))

