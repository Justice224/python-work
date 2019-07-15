from gpiozero import LED,Buzzer,Button
from time import sleep

red = LED(22)
amber = LED(27)
green = LED(17)
Buzzer = Buzzer(12)
Button =Button(2)



while True:
    Buzzer.on()
    sleep(1)
    Buzzer.off()
    red.on()
    sleep(5)
    red.off()
    amber.on()
    sleep(2)
    amber.off()
    green.on()
    sleep(5)
    green.off()
    
    
