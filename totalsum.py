n = 25
sum = 0
average = 0
for i in range(1,n,2):
    sum += i
    average = sum/n
print(f'Total Sum is {sum}')
print(f'Average is {average}')