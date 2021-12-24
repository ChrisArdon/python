row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1])


if row == 1:
    if column == 1:
        row1 = ["X","⬜️","⬜️"]
    elif column == 2:
        row1 = ["⬜️","X","⬜️"]
    else:
        row1 = ["⬜️","⬜️","X"]
elif row == 2:
    if column == 1:
        row2 = ["X","⬜️","⬜️"]
    elif column == 2:
        row2 = ["⬜️","X","⬜️"]
    else:
        row2 = ["⬜️","⬜️","X"]
elif row == 3:
    if column == 1:
        row3 = ["X","⬜️","⬜️"]
    elif column == 2:
        row3 = ["⬜️","X","⬜️"]
    else:
        row3 = ["⬜️","⬜️","X"]
else:
    print("Something's wrong")

print(f"{row1}\n{row2}\n{row3}")