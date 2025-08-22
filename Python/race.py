from turtle import Turtle
import time
import math
import random

def clamp(value, min, max):
    if value > max:
        return max
    elif value < min:
        return min
    else:
        return value

def drawTrack(radius, midlength, turtle):
    turtle.speed(0)
    turtle.up()
    turtle.sety(turtle.ycor() + radius)
    turtle.down()

    turtle.forward(midlength / 2)

    quality = 20
    halfCircumference = math.pi * radius
    stepDistance = halfCircumference / quality
    turnAmount = 180 / quality

    for steps in range(quality):
        turtle.forward(stepDistance)
        turtle.right(turnAmount)

    turtle.forward(midlength)

    for steps in range(quality):
        turtle.forward(stepDistance)
        turtle.right(turnAmount)

    turtle.forward(midlength / 2)

def initRacerPositions(racerList : list[Turtle], radius, midlength, gapSize, speed, width):
    for racer in racerList:
        racer.speed(5)
        racer.width()
        racer.up()
        racer.sety(racer.ycor() + radius)
        racer.down()

        radius -= gapSize
        midlength -= gapSize

def startRace(racerList : list[Turtle], radius, midlength, gapSize, minStepSize, maxStepSize):
    for i in range(len(racerList)):
        
        stepDistance = random.uniform(minStepSize, maxStepSize) * (1 - 0.015 * math.pi * i)
        turnAmount = (360 * stepDistance) / (2 * math.pi * (radius - gapSize * i))

        if racerList[i].xcor() >= midlength / 2 - gapSize * i:
            racerList[i].forward(stepDistance)
            racerList[i].right(turnAmount)

            racerList[i].setheading(clamp(
                racerList[i].heading(),
                180,
                360
            ))

        elif racerList[i].xcor() <= gapSize * i - midlength / 2: 
            racerList[i].forward(stepDistance)
            racerList[i].right(turnAmount)

            if 180 < racerList[i].heading() <= 360:
                racerList[i].setheading(0)
            
        elif math.ceil(racerList[i].ycor()) >= radius - gapSize * i:
            racerList[i].sety(radius - gapSize * i)
            racerList[i].forward(random.uniform(minStepSize, maxStepSize) * (1 - 0.015 * math.pi * i))
            racerList[i].setx(clamp(
                racerList[i].xcor(),
                gapSize * i - midlength / 2,
                midlength / 2 - gapSize * i
            ))

        elif math.floor(racerList[i].ycor()) <= gapSize * i - radius:
            racerList[i].sety(gapSize * i - radius)
            racerList[i].forward(random.uniform(minStepSize, maxStepSize) * (1 - 0.015 * math.pi * i))
            racerList[i].setx(clamp(
                racerList[i].xcor(),
                gapSize * i - midlength / 2,
                midlength / 2 - gapSize * i
            ))

        if round(racerList[i].ycor()) == radius - gapSize * i and (
           -10 <= racerList[i].xcor() <= 0
        ):
            racerList[i].clear()
            

        


# init racers
racer_1 = Turtle()
racer_1.color("salmon")

racer_2 = Turtle()
racer_2.color("black")
racer_2.screen.register_shape("freaky.gif")
racer_2.shape("freaky.gif")

racer_3 = Turtle()
racer_3.color("blue")

racer_4 = Turtle()
racer_4.color("red")

racer_5 = Turtle()
racer_5.color("pink")

racerList = [
    racer_1,
    racer_2,
    racer_3,
    racer_4,
    racer_5
]

radius = 200
midlength = 250
gapSize = 10
speed = 1
width = 0
minStepSize = 0
maxStepSize = 10


baseTurtle = Turtle()
baseTurtle.screen.tracer()
baseTurtle.screen.delay(0)
#drawTrack(200, 250, baseTurtle)

initRacerPositions(racerList, radius, midlength, gapSize, speed, width)

while True:
    startRace(racerList, radius, midlength, gapSize, minStepSize, maxStepSize)
    baseTurtle.setheading(baseTurtle.towards(racerList[0].pos()))

baseTurtle.screen.mainloop()