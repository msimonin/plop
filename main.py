def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global compteur
    compteur += 1
    radio.send_number(compteur)
input.on_button_pressed(Button.A, on_button_pressed_a)

compteur = 0
basic.show_icon(IconNames.HEART)
compteur = 0
radio.set_group(193)
radio.send_number(0)

def on_forever():
    pass
basic.forever(on_forever)
