a = input().split()  #Enter space-separated integers

count = {}
for i in range(1, 10):
    count[i] = 0

for num in a:
    num=int(num)
    for i in range(1, 10):
        if num % i == 0: 
            count[i] += 1

print(count)
