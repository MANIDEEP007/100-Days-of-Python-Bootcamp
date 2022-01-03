'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
Reboorg World is way to learn programming with animation
It has predefined function to move robot. But there is no predefined function for turn right & turn around
'''

#Function to turn the robot right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Function to turn the robot around
def turn_around():
    turn_left()
    turn_left()

#Code to draw the square in Reboorg World
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
turn_around()
