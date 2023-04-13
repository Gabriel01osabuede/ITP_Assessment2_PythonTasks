print("Welcome to the Multiplication Table.")
print("To get the multiplication of a number.")

result = 0
increment = 1 #Creating a Increment Variable.

value = int(input("Enter a valid number : "))
# Using a while loop to iterate through the first 10 numbers.
while increment <= 10:
    result = value * increment
    print("{0} x {1} = {2}".format(value, increment, result))
    increment += 1
    

