from machine import Pin, PWM
import utime
from rotary_encoder import RotaryEncoder
from potentiometer import Pot
from key import Key
from controller import Controller
from piano import piano

rot_enc_r = RotaryEncoder(1, 2, 0, name="Right")
pot = Pot(28)
rot_enc_l = RotaryEncoder(22, 27, 26, name="Left")

key_1 = Key(5, "K1")
key_2 = Key(4, "K2")
key_3 = Key(3, "K3")

key_4 = Key(8, "K4")
key_5 = Key(7, "K5")
key_6 = Key(6, "K6")


key_7 = Key(11, "K7")
key_8 = Key(10, "K8")
key_9 = Key(9, "K9")

led_1 =  PWM(Pin(12))
led_2 =  Pin(21, Pin.OUT) 

audio =  PWM(Pin(20))


contoller = Controller(rot_enc_l, pot, rot_enc_r,
                 key_1, key_2, key_3,
                 key_4, key_5, key_6,
                 key_7, key_8, key_9,
                 led_1, led_2, audio)

while True:
    piano(contoller)
    
    
    