'''
You are going to write a program which will mark a spot with an X.
In the starting code, you will find a variable called map.
This map contains a nested list. When map is printed this is what the nested list looks like:
['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
Specify co-ordinates in column row format 
Examples : 23, 31 are sample inputs
'''
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Get the Column & Row from Position
column =  int(position[0])
row = int(position[1])

#Set Given Position to X
map[row-1][column-1] = "X"


# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
