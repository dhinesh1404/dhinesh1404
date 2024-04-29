#Receive input from the user as one of "left", "right", "up", and "down".
direction = input("Enter a direction (left, right, up, down): ")

#Decide the message based on the input direction.
if direction == "left":
    print("move to the left")
elif direction == "right":
    print("move to the right")
elif direction == "up":
    print("move to the up")
elif direction == "down":
    print("move to the down")
else:
    print("unknown command")