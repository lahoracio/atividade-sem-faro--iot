from machine import Pin 
from utime import sleep 

print("Hello, World!")

led_vermelho = Pin(15, Pin.OUT)
led_amarelo= Pin(2, Pin.OUT)
led_verde= Pin(17, Pin.OUT)
while True:
  led_vermelho.on()
  print("Led vermelho ON!")
  sleep(7)
  led_vermelho.off()
  print("Led vermelho OFF!")
  sleep(0.5)

  led_amarelo.on()
  print("Led amarelo ON!")
  sleep(10)
  led_amarelo.off()
  print("Led amarelo OFF!")
  sleep(0.5)

  led_verde.on()
  print("Led verde ON!")
  sleep(20)
  led_verde.off()
  print("Led verde OFF!")
  sleep(0.5)


