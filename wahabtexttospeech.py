import PySimpleGUI as sg
import pyttsx3

Speech_Engine = pyttsx3.init()
Voice_Kind = Speech_Engine.getProperty('voices')



layout = [    [sg.Text('Select the type of voice:',text_color='#937ac2',background_color='#2313d1'),sg.Radio('Male', 'RADIO1', default=True, key='male',background_color='violet'),sg.Radio('Female', 'RADIO1', key='female',background_color='violet')],
     [sg.Text('Enter text to speak:',text_color='#330c31',background_color='#bad9c2',)],
          
    [sg.InputText(key='input'),sg.Button('Speak',button_color='#1bab3f')],
   [sg.Text("Volume:",text_color= 'black',background_color='silver')],
    [sg.Slider(range=(0, 1), resolution=0.1, default_value=0.5, orientation="h", key="-VOLUME-")],
    [sg.Text("Speed:",text_color= 'black',background_color='silver')],
    [sg.Slider(range=(100, 300), resolution=10, default_value=200, orientation="h", key="-SPEED-")],
     
     ]

window = sg.Window('OTAW text-to-speech', layout,background_color='#c7e80e')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        volume = values["-VOLUME-"]
        speed = values["-SPEED-"]
        if values['male']:
            Speech_Engine.setProperty('voice', Voice_Kind[0].id)
        elif values['female']:
           Speech_Engine.setProperty('voice', Voice_Kind[1].id) 
        Speech_Engine.setProperty("volume", volume)
        Speech_Engine.setProperty("rate", speed)
        Speech_Engine.say(text)
        Speech_Engine.runAndWait()

window.close()