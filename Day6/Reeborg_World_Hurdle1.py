'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
Reboorg World is way to learn programming with animation
It has predefined function to move robot. But there is no predefined function for turn right & turn around
'''

#Function to turn the robot right
def turn_right():
    for _ in range(3):
        turn_left()

#Function to take step for over one hurdle
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#So calling jump functions 6 times as there are 6 hurdles in given problem
for _ in range(6):
    jump()
