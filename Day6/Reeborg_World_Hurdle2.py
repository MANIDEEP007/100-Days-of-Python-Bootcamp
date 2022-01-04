'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
Reboorg World is way to learn programming with animation
It has predefined function to move robot. But there is no predefined function for turn right & turn around
at_goal() function returns whether we have reached flag or not. 
It will randomly put a flag between 6 hurdles and we should reach it using while loops
'''
#Function to turn the robot right
def turn_right():
    for _ in range(3):
        turn_left()

#Function to take step for over one hurdle
def step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#Until Reaching Goal, start jumping hurdles
while not at_goal():
    step()
