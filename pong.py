import turtle

BACKGROUND_COLOR = "black"
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000

window = turtle.Screen()

window.title("Pong")
window.bgcolor(BACKGROUND_COLOR)
window.setup(SCREEN_HEIGHT, SCREEN_WIDTH)
window.tracer(0)

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape('triangle')
paddle_1.color('green')
paddle_1.shapesize(stretch_len=5, stretch_wid=10)
paddle_1.penup()
paddle_1.goto(-450, 0)

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape('triangle')
paddle_2.color('green')
paddle_2.shapesize(stretch_len=5, stretch_wid=10)
paddle_2.tilt(180)
paddle_2.penup()
paddle_2.goto(450, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('green')
ball.penup()
ball.goto(0, 0)

while True:
    window.update()
