from machine import Pin, Timer


def tick(timer):
    global led
    led.toggle()


led = Pin(25, Pin.OUT)
tim = Timer()

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)
