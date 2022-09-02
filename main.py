from machine import Pin, Timer, ADC
import utime
import rp2



def tick(timer):
    global led
    led.toggle()


led = Pin(25, Pin.OUT)
tim = Timer()

tim.init(freq=.3, mode=Timer.PERIODIC, callback=tick)


sensor_temp = ADC(4)
conversion_factor = 3.3 / (2 ** 16 - 1)

eled = Pin(15, Pin.OUT)

while True:
    reading = sensor_temp.read_u16() * conversion_factor

    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to
    # the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
    c_temp = 27 - (reading - 0.706)/0.001721
    f_temp = c_temp * 9/5 + 32
    print(f'{c_temp}C, {f_temp}F')
    eled.value(True)
    utime.sleep(2)
    eled.value(False)
    utime.sleep(2)
