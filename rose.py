import turtle
import winsound

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")

# Create a new turtle object
rose = turtle.Turtle()
rose.speed(0)

# Function to draw a rose
def draw_rose(turt, color, size):
    turt.fillcolor(color)
    turt.begin_fill()
    for _ in range(36):
        turt.forward(size)
        turt.left(170)
    turt.end_fill()

# Draw a rose
draw_rose(rose, "red", 100)

# Add background music
winsound.PlaySound("music.mid", winsound.SND_ASYNC)

# Keep the window open
turtle.done()
