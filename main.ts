radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    basic.showNumber(receivedNumber)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    compteur += 1
    radio.sendNumber(compteur)
})
let compteur = 0
basic.showIcon(IconNames.Heart)
compteur = 0
radio.setGroup(193)
radio.sendNumber(0)
basic.forever(function on_forever() {
    
})
