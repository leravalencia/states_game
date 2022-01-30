import turtle
import turtle as t
import pandas as pd

screen= t.Screen()
screen.title('State Game')
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)
counter = 0
correct_answers = []

non_listed_states = []

states = pd.read_csv('50_states.csv')

while counter<50:
    answer_state = screen.textinput(title="what's the state name", prompt='type the state that you know').title()
    if answer_state == 'Exit':
        for state in states['state'].values:
            if state not in correct_answers:
                non_listed_states.append(state)
                new_data = pd.DataFrame(non_listed_states)
                new_data.to_csv('need_to_know.csv')
        turtle.goto(-200, 0)
        turtle.write(f'You won! your score is {counter}, your states are {counter}/{len(states["state"])}',
                     font={'Arial', 245})
        turtle.goto(100, -100)
        turtle.write(new_data)
        break
    if answer_state in states['state'].values:
        turtle = t.Turtle()
        turtle.hideturtle()
        turtle.penup()
        counter +=1
        correct_answers.append(answer_state)
        xcor = int(states.loc[states['state'] == answer_state]['x'])
        ycor = int(states.loc[states['state'] == answer_state]['y'])
        turtle.goto(xcor,ycor)
        turtle.write(answer_state)
        if counter >= len(states['state']):
            game_is_on = False
            turtle.goto(-100, 0)
            final_list = pd.read_csv('final_list.csv').truncate()
            final_list = pd.DataFrame(correct_answers).to_csv('final_list.csv')
            turtle.write(f'You won! your score is {counter}, your states are {counter}/{len(states["state"])}', font={'Arial', 145})
    else:
        turtle2 = t.Turtle()
        turtle2.hideturtle()
        turtle2.goto(-40, 0)
        turtle2.write('you wrong, there is no such a state, try again', font={'Arial', 145})
        turtle2.clear()


t.update()

t.mainloop()
screen.exitonclick()
