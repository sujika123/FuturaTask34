# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five If the number is greater than 150, then skip it and
# move to the next number If the number is greater than 500, then stop the loop


#Method1

# List of numbers
numbers = [12, 75, 150, 180, 145, 525, 50]

# Iterate over the numbers in the list
for num in numbers:
    if num > 500:
        break  # Stop the loop if the number is greater than 500
    if num > 150:
        continue  # Skip the number if it is greater than 150
    if num % 5 == 0:
        print(num)  # Print the number if it is divisible by 5


print("________________________________________")

#Method2

numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)