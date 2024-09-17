# Take input from user
rows = int(input("Please Enter the total Number of Rows  : "))
number = 1  # Initialize by 1

print("\nFloyd's Triangle") 

# Outer loop for the number of rows
for i in range(1, rows + 1):
    # Inner loop for the number of columns in each row
    for j in range(1, i + 1):   
        # Display the current number
        print(number, end='  ')
        number += 1  # Increment the number for the next print
    print()  # Move to the next line after each row is printed5
    