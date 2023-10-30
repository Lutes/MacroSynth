from machine import ADC


class Pot:
    def __init__(self, anolog_pin_num):
        self.ADC_PIN = ADC(anolog_pin_num)
    def get_value(self):
        return (self.ADC_PIN.read_u16()/65535) # 65535 is the max value. 
    def get_raw_value(self):
        return self.ADC_PIN.read_u16() 
        
