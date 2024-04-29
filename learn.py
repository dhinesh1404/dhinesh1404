import random

bar  = list()
for _ in range(0, 5):
    bar.append(random.randint(1, 100))
    
print(bar)

#[90, 50, 30, 100, 20]

print(bar [4], bar[-1], bar[len(bar) - 1] )