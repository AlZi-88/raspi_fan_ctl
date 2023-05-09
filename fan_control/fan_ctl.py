from fan import fan
import time

class fan_control:
    def __init__(self, onTime, offTime, fan_pin=27)
        self.onTimeSp = onTime
        self.offTimeSp = offTime
        self.fan = fan.fan(fan_pin)
        self.TimeOn = 0.0
        self.TimeOff = 0.0
        self.Time = time.time()
        self.status = self.fan.get_status()
        
    def update_TimeOn(self):
        self.TimeOn = time.time() - self.Time
    def update_TimeOff(self):
        self.TimeOff = time.time() - self.Time
    def update_Time(self):
        self.Time = time.time()
    def update_onTimeSp(onTime):
        self.onTimeSp = onTime
    def update_offTimeSp(offTime):
        self.offTimeSp = offTime
