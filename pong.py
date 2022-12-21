import turtle

BACKGROUND_COLOR = "black"
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000

# Window
window = turtle.Screen()
window.title("Pong")
window.bgcolor(BACKGROUND_COLOR)
window.setup(SCREEN_HEIGHT, SCREEN_WIDTH)
window.tracer(0)

# Paddel 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape('triangle')
paddle_1.color('green')
paddle_1.shapesize(stretch_len=5, stretch_wid=10)
paddle_1.penup()
paddle_1.goto(-450, 0)

# Paddel 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape('triangle')
paddle_2.color('green')
paddle_2.shapesize(stretch_len=5, stretch_wid=10)
paddle_2.tilt(180)
paddle_2.penup()
paddle_2.goto(450, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('green')
ball.penup()
ball.goto(0, 0)
ball.ax = 0.7
ball.ay = 0.7


# Paddle Mechanics
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


window.listen()
window.onkeypress(paddle_1_up, 'w')
window.onkeypress(paddle_1_down, 's')
window.onkeypress(paddle_2_up, 'Up')
window.onkeypress(paddle_2_down, 'Down')

while True:
    window.update()

    ball.setx(ball.xcor() + ball.ax)
    ball.sety(ball.ycor() + ball.ay)
