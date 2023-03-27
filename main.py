import os.path
import time
import PySimpleGUI as sg
import qrcode as qr

# layout
input_box = sg.Input('Enter text here', key='input')
create_button = sg.Button('Create', key='create')
box_size = sg.Slider((0, 10), 5, key='size', orientation='h', enable_events=True)
generated_qr = sg.Image(key='QRCODE', size=(300, 30),expand_y=True,expand_x=True)
layout = [
    [input_box],
    [create_button],
    # [sg.Text('Adjust the size'), box_size],
    [generated_qr]
]

window = sg.Window('QR Code Generate', font='11', layout=layout)


def generate_qrcode(data):
    code = qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5)
    code.add_data(data)
    code.make(fit=True)
    image = code.make_image(
        fill_color='black',
        back_color='white')
    file_name = 'qr_code.png'
    path = os.path.join(os.getcwd(), file_name)
    image.save(path)
    return path


while True:
    event, values = window.read()
    # QUITTING
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'create':
        address = values['input']
        qr_code_image_path = generate_qrcode(address)
        window['QRCODE'].update(filename=qr_code_image_path)
window.close()
