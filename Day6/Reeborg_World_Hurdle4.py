'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
Reboorg World is way to learn programming with animation
It has predefined function to move robot. But there is no predefined function for turn right & turn around
at_goal() function returns whether we have reached flag or not. 
front_is_clear() returns whether we have wall in front or not
right_is_clear() returns whether we have wall at right or not
It will wall at random places and we should reach it using while loops
'''

#Function to turn the robot right
def turn_right():
    for _ in range(3):
        turn_left()

#Function to take step for over one hurdle of random length
def step():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

#Until Goal is not reached
while not at_goal():
    #If frong wall is not there, move one step  
    if front_is_clear():
        move()
    #If front wall is there, make jump over it        
    else:
        step()
