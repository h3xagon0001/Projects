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
bodyOne.shapesize(1, 1)
bodyOnePhysics = {
    "mass": 2000.0,
    "x_position": 0.0,
    "y_position": 0.0,
    "x_velocity": 0.0,
    "y_velocity": 0.0
}
bodyOne.teleport(bodyOnePhysics["x_position"], bodyOnePhysics["y_position"])


bodyTwo = t.Turtle()
bodyTwo.penup()
bodyTwo.pensize(1)
bodyTwo.color("blue")
bodyTwo.shape("circle")
bodyTwo.shapesize(0.25, 0.25)
bodyTwoPhysics = {
    "mass": 0.1,
    "x_position": 1500.0,
    "y_position": 0.0,
    "x_velocity": 0.0,
    "y_velocity": 30.0
}
bodyTwo.teleport(bodyTwoPhysics["x_position"], bodyTwoPhysics["y_position"])


bodyThree = t.Turtle()
bodyThree.penup()
bodyThree.pensize(1)
bodyThree.color("green")
bodyThree.shape("circle")
bodyThree.shapesize(0.5, 0.5)
bodyThreePhysics = {
    "mass": 50.0,
    "x_position": 1700.0,
    "y_position": 0.0,
    "x_velocity": 0.0,
    "y_velocity": 40.0
}
bodyThree.teleport(bodyThreePhysics["x_position"], bodyThreePhysics["y_position"])

bodies = [bodyOnePhysics, bodyTwoPhysics, bodyThreePhysics]
turtleBodies = [bodyOne, bodyTwo, bodyThree]

root.screen.delay(1)
bodyOne.pendown(); bodyTwo.pendown(); bodyThree.pendown()

while True:
    for i in range(len(bodies)):
        for j in range(len(bodies)):
            if bodies[j] != bodies[i]:
                force = getGravForce(
                    bodies[i]["mass"],
                    bodies[j]["mass"],
                    turtleBodies[i].distance(turtleBodies[j]),
                    1000
                )

                bodies[i]["x_velocity"] += force * math.cos(math.radians(turtleBodies[i].towards(turtleBodies[j]))) / bodies[i]["mass"]
                bodies[i]["y_velocity"] += force * math.sin(math.radians(turtleBodies[i].towards(turtleBodies[j]))) / bodies[i]["mass"]

    bodyOne.setpos(bodyOne.xcor() + bodyOnePhysics["x_velocity"], bodyOne.ycor() + bodyOnePhysics["y_velocity"])
    bodyTwo.setpos(bodyTwo.xcor() + bodyTwoPhysics["x_velocity"], bodyTwo.ycor() + bodyTwoPhysics["y_velocity"])
    bodyThree.setpos(bodyThree.xcor() + bodyThreePhysics["x_velocity"], bodyThree.ycor() + bodyThreePhysics["y_velocity"])
