import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.title("Roulette Game")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create turtle for drawing the roulette wheel
wheel = turtle.Turtle()
wheel.speed(0)
wheel.hideturtle()

# Function to draw the roulette wheel
def draw_roulette_wheel():
    wheel.penup()
    wheel.goto(0, -250)
    wheel.pendown()
    wheel.color("black")
    wheel.begin_fill()
    wheel.circle(250)  # Draw the outer circle of the wheel
    wheel.end_fill()

    # Draw the numbers and sections
    wheel.penup()
    wheel.goto(0, 0)
    wheel.setheading(90)  # Start from top
    numbers = ["32", "15", "19", "4", "21", "2", "25", "17", "34", "6", "27", "13", "36", "11", "30", "8", "23", "10", "5", "24", "16", "33", "1", "20", "14", "31", "9", "22", "18", "29", "7", "28", "12", "35", "3", "26"]
    color_map = ["red", "black"] * 18  # Alternating red and black colors

    for i, number in enumerate(numbers):
        angle = i * 360 / len(numbers)
        wheel.penup()
        wheel.goto(0, 0)
        wheel.setheading(angle)
        wheel.forward(200)  # Move turtle to the edge of the circle
        wheel.pendown()
        wheel.color(color_map[i])
        wheel.forward(50)  # Draw a small line for each section

        # Draw the number inside the section
        wheel.penup()
        wheel.goto(0, 0)
        wheel.setheading(angle + 180)
        wheel.forward(120)
        wheel.write(number, align="center", font=("Arial", 12, "normal"))

# Create turtle for spinning the wheel
spinner = turtle.Turtle()
spinner.shape("triangle")
spinner.color("blue")
spinner.penup()
spinner.goto(0, 0)
spinner.setheading(90)

# Function to spin the wheel and select a random number
def spin_wheel():
    spin_angle = random.randint(0, 360)  # Spin the wheel by a random angle
    spinner.setheading(spin_angle)
    spinner.stamp()  # Stamp a mark to indicate spin position

    result_index = spin_angle // (360 // len(["32", "15", "19", "4", "21", "2", "25", "17", "34", "6", "27", "13", "36", "11", "30", "8", "23", "10", "5", "24", "16", "33", "1", "20", "14", "31", "9", "22", "18", "29", "7", "28", "12", "35", "3", "26"]))
    numbers = ["32", "15", "19", "4", "21", "2", "25", "17", "34", "6", "27", "13", "36", "11", "30", "8", "23", "10", "5", "24", "16", "33", "1", "20", "14", "31", "9", "22", "18", "29", "7", "28", "12", "35", "3", "26"]
    result = numbers[result_index]
    print(f"Result: {result}")

# Add a button for spinning
button = turtle.Turtle()
button.shape("square")
button.color("green")
button.penup()
button.goto(0, -300)
button.write("Click to Spin", align="center", font=("Arial", 16, "normal"))
button.onclick(lambda x, y: spin_wheel())

# Draw the roulette wheel
draw_roulette_wheel()

# Main loop to keep the window open
screen.mainloop()
