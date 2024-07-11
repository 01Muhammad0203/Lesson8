
N = int(input())

#Вывод 
numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)


reversed_numbers = numbers[::-1]


for number in reversed_numbers:
    print(number)
