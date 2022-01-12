import turtle
import pandas

from name_writer import NameWriter

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
# change the shape of turtle to image
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

# print(states_list)

correct_answers = []

# 50 states in us , while not getting all states , keep going

while len(correct_answers) < 50:
    # convert the user answer to title case
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 states Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":

        # use XOR operator to get the difference between the 2 list , return a dictionary
        # states_remain = set(correct_answers) ^ set(states_list)

        states_remain = []
        for state in states_list:
            if state not in correct_answers:
                states_remain.append(state)
        print(states_remain)

        new_data = pandas.DataFrame(states_remain)
        new_data.to_csv("states_remain.txt")
        break

    if answer_state in states_list:
        correct_answers.append(answer_state)
        state_data = data[data.state == answer_state]
        new_writer = NameWriter()
        coordinate = (int(state_data.x), int(state_data.y))
        new_writer.write_name(coordinate, answer_state)

screen.exitonclick()
