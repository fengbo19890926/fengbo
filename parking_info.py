import time
class Parking_info():
    def __init__(self,owner,car,position):
        self.owner = owner
        self.car = car
        self.position = position
        
    @staticmethod
    def time_format(s):
        timeArray = time.strptime(s, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        return timeStamp

    def time_duration(self):
        return self.time_format(self.owner.time_leave)-self.time_format(self.owner.time_in)
    
    


