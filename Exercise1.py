blocks = int(input("Enter the amount of blocks you have: "))

required = 1

floors = 0

while blocks >= required:
    floors += 1
    blocks -= required
    required += 1

print("Floors built: ", floors)
print("Blocks left: ", blocks)
print("Required for next floor: ", required)