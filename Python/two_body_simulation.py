# tweak starting positions, velocity and the constant until satisfied
# high velocity allows orbiting of heavy objects
# large constant increases pull strength


import turtle as t
import math

def getGravForce(massOne, massTwo, distance, constant):
    force = constant * massOne * massTwo / (distance ** 2)
    return force

t.setup(800, 500)
root = t.Turtle()
root.screen.setworldcoordinates(-4000, -2500, 4000, 2500)
root.screen.bgcolor("black")


bodyOne = t.Turtle()
bodyOne.penup()
bodyOne.pensize(1)
bodyOne.color("red")
bodyOne.shape("circle")
bodyOne.shapesize(0.5, 0.5)
bodyOnePhysics = {
    "mass": 2.0,
    "x_position": -3000.0,
    "y_position": 300.0,
    "x_velocity": 20.0,
    "y_velocity": -5.0
}
bodyOne.teleport(bodyOnePhysics["x_position"], bodyOnePhysics["y_position"])


bodyTwo = t.Turtle()
bodyTwo.penup()
bodyTwo.pensize(1)
bodyTwo.color("blue")
bodyTwo.shape("circle")
bodyTwo.shapesize(0.5, 0.5)
bodyTwoPhysics = {
    "mass": 2.0,
    "x_position": -3000.0,
    "y_position": -300.0,
    "x_velocity": 10.0,
    "y_velocity": 5.0
}
bodyTwo.teleport(bodyTwoPhysics["x_position"], bodyTwoPhysics["y_position"])

bodies = [bodyOnePhysics, bodyTwoPhysics]
turtleBodies = [bodyOne, bodyTwo]

root.screen.delay(1)
bodyOne.pendown(); bodyTwo.pendown()

while True:
    for i in range(len(bodies)):
        for j in range(len(bodies)):
            if bodies[j] != bodies[i]:
                force = getGravForce(
                    bodies[i]["mass"],
                    bodies[j]["mass"],
                    turtleBodies[i].distance(turtleBodies[j]),
                    50000
                )

                bodies[i]["x_velocity"] += force * math.cos(math.radians(turtleBodies[i].towards(turtleBodies[j]))) / bodies[i]["mass"]
                bodies[i]["y_velocity"] += force * math.sin(math.radians(turtleBodies[i].towards(turtleBodies[j]))) / bodies[i]["mass"]

    bodyOne.setpos(bodyOne.xcor() + bodyOnePhysics["x_velocity"], bodyOne.ycor() + bodyOnePhysics["y_velocity"])
    bodyTwo.setpos(bodyTwo.xcor() + bodyTwoPhysics["x_velocity"], bodyTwo.ycor() + bodyTwoPhysics["y_velocity"])

