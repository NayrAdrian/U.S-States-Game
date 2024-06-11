import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# Read data from CSV and convert states to lowercase
all_states = data["state"].tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                     prompt="Give a name of a state in U.S:")).title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to.csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)

states_to_learn = all_states not in guessed_states
print(states_to_learn)
