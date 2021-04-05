let sum2 = 0
let times = 0
input.onButtonPressed(Button.A, function () {
    sum2 = sum2 + 24
    times = times + 1
})
input.onButtonPressed(Button.AB, function () {
    sum2 = 24 * 24
    times = 24
})
input.onButtonPressed(Button.B, function () {
    sum2 = sum2 + 240
    times = times + 10
})
basic.forever(function () {
    basic.showString("t" + ("" + times) + "s" + ("" + sum2))
})
