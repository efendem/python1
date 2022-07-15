import random
number=list(range(1, n+1))
x=number.pop(random.randint(1, n+1))
# x ni toping

# for i in range(1, n):
#     if i not in numbers:
#         print(i)
#         break
summa = n*(n+1)/2
print(summa-sum(numbers))
