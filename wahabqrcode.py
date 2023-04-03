import PySimpleGUI as sg
import qrcode

layout = [
    [sg.Text('Enter a link to generate a QR code:', text_color='#c7e80e',background_color='#0e2433')],
    [sg.Input(key='link')],
    [sg.Text('Choose a color:',text_color='#ebe728'), sg.Combo(values=['black', 'red', 'green', 'blue'], key='color')],
    [sg.Text('Choose a size:',text_color='#ebe728'), sg.Slider(range=(1, 10), default_value=5, orientation='h', key='size')],
    [sg.Button('Generate',button_color='#ed9521'), sg.Button('Save As', button_color='#ed9521')],
    [sg.Image(key='image')]
]

window = sg.Window('QR Code Generator',layout,background_color='#383831')

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Generate':
        User_link = values['link']
        User_color = values['color']
        User_size = values['size']
        qr = qrcode.QRCode(version=1,box_size=User_size, border=3, error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(User_link)
        qr.make(fit=True)
        img = qr.make_image(fill_color=User_color, back_color='white')
        img.save('qrcode.png')
        window['image'].update('qrcode.png')
    
    # Saving the Qr code
    if event == 'Save As':
        filename = sg.popup_get_file('Save Qr Code', save_as=True, default_extension='.png')
        if filename:
            img.save(filename)
    
        

window.close()