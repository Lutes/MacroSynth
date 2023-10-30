import utime


def piano(controller):
    print("Entering Piano Mode")
    freq = 20 # Random valid freq, not heard since duty cycle is zero by default
    controller.led_1.init(freq=1000, duty_u16=5000)
    while True:   
        controller.rot_enc_l.rotary_changed()
        controller.rot_enc_r.rotary_changed()
        

        
        mult = pow(2, controller.rot_enc_l.get_value())
        
        # Sharp Shift
        if(controller.key_8.is_press()):
            sharp_modifier = 1
        else:
            sharp_modifier = 0

        if(controller.key_9.is_press()):
            duty = int(duty * (1 - pow(0.1, controller.rot_enc_r.get_value())))
        else: 
            duty = 0
            
            
        # C 
        if(controller.key_1.is_press()):
            freq = int((16.35 + sharp_modifier) * mult)
            duty = int(65535 * controller.pot.get_value())
        # D
        if(controller.key_2.is_press()):
            freq = int((18.35 + sharp_modifier) * mult)
            duty = int(65535 * controller.pot.get_value())
        # E
        if(controller.key_3.is_press()):
            freq = int((20.60 + sharp_modifier) * mult)
            duty = int(65535 * controller.pot.get_value())
        # F
        if(controller.key_4.is_press()):
            freq = int((21.83 + sharp_modifier) * mult)
            duty = int(65535 * controller.pot.get_value())
        # G    
        if(controller.key_5.is_press()):
            freq = int((24.50 + sharp_modifier) * mult)
            duty = int(65535 * controller.pot.get_value())
        # A
        if(controller.key_6.is_press()):
            freq = int((27.50 + sharp_modifier) * mult)
            duty = int(65535 * controller.pot.get_value())
        # B
        if(controller.key_7.is_press()):
            freq = int((30.87 + sharp_modifier) * mult)
            duty = int(65535 * controller.pot.get_value())

        controller.audio.freq(freq)
        controller.audio.duty_u16(duty)
        controller.led_2.init(freq=freq, duty_u16=duty)
        
        
        if (controller.rot_enc_r.is_pressed()):
            controller.audio.duty_u16(0)
            controller.led_2.duty_u16(0)
            print("Leaving Piano Mode")
            break
        
        utime.sleep(0.001)
