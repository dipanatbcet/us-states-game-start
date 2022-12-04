import turtle
import pandas

# reading csv data and storing in data variable
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
screen = turtle.Screen()
# window name
screen.title("U.S. State Name Quiz")
# registering image to be used in shape method later
image = "blank_states_img.gif"
screen.addshape(image)
# using the image in screen output
turtle.shape(image)
correct_state_list = []
user_score = len(correct_state_list)

tim = turtle.Turtle()
# checking if user guess is correct or not
n = 0
answer_state = screen.textinput(title=f"{user_score}/{len(state_list)} States correct",
                                prompt="What's another state name?").title()
while n < len(state_list):
    if answer_state == 'Exit':
        break
    for index in state_list:
        if answer_state == index:
            correct_state_list.append(index)
            answer_x_pos = int(data[data.state == answer_state].x)
            answer_y_pos = int(data[data.state == answer_state].y)
            tim.ht()
            tim.penup()
            tim.goto(answer_x_pos, answer_y_pos)
            tim.write(answer_state, True, align='left', font=('Arial', 8, 'bold'))
            n += 1
    user_score = len(correct_state_list)
    answer_state = screen.textinput(title=f"{user_score}/{len(state_list)} States correct",
                                    prompt="What's another state name?").title()

# list of state names which user could not guess
state_to_know = []
for i in state_list:
    for j in correct_state_list:
        if j != i:
            state_to_know.append(i)

# creating file with state name which user could not guess
data_dict = {"State_Name": state_to_know}
pandas.DataFrame(data_dict).to_csv("state_to_know.csv")
