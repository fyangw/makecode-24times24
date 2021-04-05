sum2 = 0
times = 0

def on_button_pressed_a():
    global sum2, times
    sum2 = sum2 + 24
    times = times + 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global sum2, times
    sum2 = 24*24
    times = 24
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global sum2, times
    sum2 = sum2 + 240
    times = times + 10
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_string("t" + ("" + str(times)) + "s" + ("" + str(sum2)))
basic.forever(on_forever)
