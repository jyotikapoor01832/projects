""" Write a python program which will keep adding a stream of numbers inputted by the user.
The adding stops as soon as user presses q key on the keyboard."""

sum = 0
while (True):
    UserInput = input("Enter the item price or press q to quit :\n")
    
    if UserInput != 'q':
        sum = sum + int(UserInput)
        print(f"Sum of prices is : ₹ {sum}")
    else:
        print(f"Your total bill is : ₹ {sum} .")
        print(" ----Thanks for shopping with us ----")
        break