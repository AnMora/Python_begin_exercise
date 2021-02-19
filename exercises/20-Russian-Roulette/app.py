import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return "espacio: " + chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    if bullet_position == spin_chamber:
        print("You are dead!")
    else:
        print("Keep playing")

    #return "You are dead!" if bullet_position == spin_chamber() else "Keep playing"

print(fire_gun())