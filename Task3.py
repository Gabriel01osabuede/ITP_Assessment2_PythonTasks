print("\nFor loop")
for i in range(1, 10):
    print("{} x {} = {}".format(i,i, i*i))


print("\nWhile loop equivalent")
i = 1
while i < 10:
    print("{} x {} = {}".format(i, i, i*i)) 
    i+=1
    if(i > 10):
        break

sum = 0
for i in range  (10,0, -1):
    sum = sum + i
print(i, sum)