import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian State Quiz")
screen.setup(700, 780)

image = "India_Map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("India_States.csv")
all_states = data["State/ UT"].to_list()
guessed_states = []

while len(guessed_states) < 36:
    answer = screen.textinput(title=f"{len(guessed_states)}/36 States/UT Correct",
                              prompt="What's another state's name ?").title()
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
            states_to_learn = pandas.DataFrame(missing_states)
            states_to_learn.to_csv("States_to Learn.csv")
        break

    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.pencolor("green")
        state_data = data[data["State/ UT"] == answer]
        t.goto(int(state_data.X), int(state_data.Y))
        t.write(answer)


