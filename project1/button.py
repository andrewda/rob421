from gpiozero import Button

button = Button(10)

button.wait_for_press()
print("Button was pressed")
