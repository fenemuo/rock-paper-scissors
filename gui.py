import random
import os
import PySimpleGUI as sg

CHOICES = ['rock', 'paper', 'scissors']
IMG_DIR = os.path.join(os.path.dirname(__file__), 'assets')  # optional images folder

def decide_result(user, comp):
    if user == comp:
        return "It's a tie!"
    wins = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    return "You win!" if wins[user] == comp else "You lose!"

def image_for(choice):
    path = os.path.join(IMG_DIR, f"{choice}.png")
    return path if os.path.exists(path) else None

def main():
    sg.theme('DarkBlue3')
    img_rock = image_for('rock')
    img_paper = image_for('paper')
    img_scissors = image_for('scissors')

    button_row = []
    for label, img in (('Rock', img_rock), ('Paper', img_paper), ('Scissors', img_scissors)):
        if img:
            button_row.append(sg.Button(label, size=(10,2), image_filename=img, image_subsample=2))
        else:
            button_row.append(sg.Button(label, size=(10,2)))

    layout = [
        [sg.Text('Rock, Paper, Scissors', font=('Any', 16), justification='center', expand_x=True)],
        [sg.Text('Choose one:')],
        button_row,
        [sg.Text('Computer chose:'), sg.Text('', key='-COMP-')],
        [sg.Text('Result:'), sg.Text('', key='-RESULT-', font=('Any', 14), text_color='yellow')],
        [sg.Button('Quit')]
    ]

    window = sg.Window('RPS GUI', layout, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Quit'):
            break
        if event in ('Rock', 'Paper', 'Scissors'):
            user_choice = event.lower()
            comp_choice = random.choice(CHOICES)
            result = decide_result(user_choice, comp_choice)
            window['-COMP-'].update(comp_choice)
            window['-RESULT-'].update(result)

    window.close()

if __name__ == '__main__':
    main()