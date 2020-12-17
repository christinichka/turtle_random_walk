import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Turtle goes in one of 4 directions randomly
# Turtle line is thick
# Speed up the Turtle so it draws faster

speed = 0
directions = [0, 90, 180, 270]

for _ in range(200):
  tim.forward(50)
  tim.setheading(random.choice(directions))
  tim.pensize(20)
  tim.color(random.choice(colors))
