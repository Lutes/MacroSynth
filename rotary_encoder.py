from machine import Pin
import utime

class RotaryEncoder():
    def __init__(self, pin_num_clk, pin_num_dt, pin_num_sw, min_val=0, max_val=9, incr=1, name="Rot"):
        self.DT_Pin = Pin(pin_num_clk, Pin.IN, Pin.PULL_UP)
        self.CLK_Pin = Pin(pin_num_dt, Pin.IN, Pin.PULL_UP)
        self.SW = Pin(pin_num_sw, Pin.IN, Pin.PULL_UP)
        self.max_val = max_val
        self.previousValue = 1
        self.value = 0
        self.name = name
        
    def rotary_changed(self):       
        if self.previousValue != self.CLK_Pin.value():
            if self.CLK_Pin.value() == 0:
                if self.DT_Pin.value() == 0:
                    self.value = (self.value + 1)%self.max_val
                    print(f"{self.name}: anti-clockwise - {self.value}")
                else:
                    self.value = (self.value - 1)%self.max_val
                    print(f"{self.name}: clockwise - {self.value}")                
            self.previousValue = self.CLK_Pin.value()
                      
    def is_pressed(self):
        return not self.SW.value() 
        
    def get_value(self):
        return self.value