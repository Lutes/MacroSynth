from machine import Pin

class Key:
    def __init__(self, pin_num, name="Key"):
        self.DIG_PIN = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        self.name = name
        
    def get_value(self):
        return (self.DIG_PIN.value())
    
    def is_press(self):
        return (not self.DIG_PIN.value())
        
    def get_value_str(self):
        return f"Pressed - {self.name} - {self.DIG_PIN.value()}"