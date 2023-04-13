print("Welcome to Task 1 solutions.\n")
print("\nTask 1 Print first 10 numbers using while loop")
i = 1
while i < 20:
    if (i > 10):
        break
    print(i)
    i += 1

print("\nPrint first 10 even numbers using for loop")
for evenNumber in range(0, 22):
    if (evenNumber % 2 == 0):
        print(evenNumber)
    
print("\nPrint first 10 odd numbers using while loop")
oddNumber = 0
while oddNumber <= 20:
    if(oddNumber > 20):
        break
    if(oddNumber % 2 != 0):
        print(oddNumber)
    oddNumber += 1
    
print("\nPrint sum of first 10 numbers using for loop")
Total = 0
loopCount = 0
for addNumbers in range(1, 20):
    # Adding the sum of the current number to the total of the previous number
    Total = addNumbers + Total
    print(Total)
    loopCount+=1 #loop count increment
    # Checking the loop count
    if(loopCount >= 10):
        break
    
    
    
     
    

    
    