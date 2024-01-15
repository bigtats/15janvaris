import PySimpleGUI as sg
layout=[
    [sg.Text('Ievadīt vārdu'),sg.InputText(key='-IN-', enable_events=True)],
    [sg.Text('Ievadīt uzvārdu'),sg.InputText(key='-INN-', enable_events=True)],
    [sg.Butoon('ok')]

]

window=sg.window('Ziema', layout)
while True:
    event, values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=='OK':
        print(values['-IN-'])
        