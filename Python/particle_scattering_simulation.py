import turtle as t
import random
import math


def getElectrostaticForce(chargeOne: int, chargeTwo: int, distance: float, constant: float):
    force = constant * chargeOne * chargeTwo / (distance ** 2)
    return force


t.setup(800, 400)
t.Turtle().screen.setworldcoordinates(0, 0, 800, 400)
t.Turtle().screen.bgcolor("black")
t.Turtle().screen.delay(0)


alphaParticle = t.Turtle()
alphaParticle.color()
alphaParticle.shape("circle")
alphaParticle.color("red")
alphaParticle.shapesize(0.25, 0.25)
alphaParticle.penup()
alphaParticle.pensize(1)
alphaParticle.screen.delay(1) # change this for speed

mass = 2
xVelocity = 4
yVelocity = 0


goldNuclei: list[t.Turtle] = []

for i in range(15):
    goldNuclei.append(t.Turtle())
    goldNuclei[i].shape("circle")
    goldNuclei[i].color("gold")
    goldNuclei[i].shapesize(0.5, 0.5)
    goldNuclei[i].penup()

    if i in range(0, 5):
        goldNuclei[i].teleport(350, 60 + 80*i)

    elif i in range(5, 10):
        goldNuclei[i].teleport(400, 20 + 80*(i-5))

    else:
        goldNuclei[i].teleport(450, 60 + 80*(i-10))


alphaParticle.teleport(10, random.uniform(10, 390))

while True:
    alphaParticle.pendown()

    if alphaParticle.xcor() < 0 or alphaParticle.xcor() > 800:
        alphaParticle.teleport(10, random.uniform(10, 390))
        xVelocity = 4
        yVelocity = 0
        alphaParticle.clear()

    elif alphaParticle.ycor() < 0 or alphaParticle.ycor() > 400:
        alphaParticle.teleport(10, random.uniform(10, 390))
        xVelocity = 4
        yVelocity = 0
        alphaParticle.clear()

    else:
        for nuclei in goldNuclei:
            force = getElectrostaticForce(
                chargeOne = 2,
                chargeTwo = 79,
                distance = alphaParticle.distance(nuclei),
                constant = 0.25
            )

            xForce = force * math.cos(math.radians(alphaParticle.towards(nuclei)))
            xVelocity -= xForce / mass

            yForce = force * math.sin(math.radians(alphaParticle.towards(nuclei)))
            yVelocity -= yForce / mass

        alphaParticle.setpos(
        alphaParticle.xcor() + xVelocity,
        alphaParticle.ycor() + yVelocity
    )