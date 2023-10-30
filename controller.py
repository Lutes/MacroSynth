class Controller:
    def __init__(self, rot_enc_l, pot, rot_enc_r,
                 key_1, key_2, key_3,
                 key_4, key_5, key_6,
                 key_7, key_8, key_9,
                 led_1, led_2, audio):
        self.rot_enc_l = rot_enc_l
        self.pot = pot
        self.rot_enc_r = rot_enc_r
        self.key_1 = key_1
        self.key_2 = key_2
        self.key_3 = key_3
        self.key_4 = key_4
        self.key_5 = key_5
        self.key_6 = key_6
        self.key_7 = key_7
        self.key_8 = key_8
        self.key_9 = key_9
        
        self.led_1 = led_1
        self.led_2 = led_2
        
        self.audio = audio