import turtle

t = turtle.Turtle()
t.speed(3)
t.hideturtle()

# Parameters
CIRCLE_RADIUS = 40
STEM_WIDTH = 20
STEM_HEIGHT = 300  # vertical line length
SHIFT_UP = 150      # move the whole T up

# ===== Draw the two touching circles at the bottom =====
# Left circle
t.penup()
t.goto(-CIRCLE_RADIUS, -CIRCLE_RADIUS - STEM_HEIGHT + SHIFT_UP)  # center left
t.pendown()
t.circle(CIRCLE_RADIUS)

# Right circle
t.penup()
t.goto(CIRCLE_RADIUS, -CIRCLE_RADIUS - STEM_HEIGHT + SHIFT_UP)   # center right
t.pendown()
t.circle(CIRCLE_RADIUS)

# ===== Draw vertical stem going down from top and touching the circles =====
t.penup()
t.goto(-STEM_WIDTH/2, SHIFT_UP)  # top-left corner of stem at top
t.pendown()

for _ in range(2):
    t.forward(STEM_WIDTH)
    t.right(90)
    t.forward(STEM_HEIGHT)
    t.right(90)

turtle.done()