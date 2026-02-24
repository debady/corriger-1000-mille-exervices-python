from random import randrange
import turtle 
monrayon=randrange(300,301)
print("le rayon choisir est ",monrayon)
turtle.color('black', 'green')
turtle.begin_fill()
turtle.circle(monrayon)
turtle.end_fill()
