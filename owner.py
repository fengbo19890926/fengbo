class Owner():
    def __init__(self,name,car,time_in=0,time_park=0,time_go=0,time_leave=0):
        self.name = name
        self.car = car
        self.time_in = time_in
        self.time_park = time_park
        self.time_go = time_go
        self.time_leave = time_leave
        
    def drive_in(self,time_in):
        self.time_in = time_in
        

    def drive_park(self,time_park):
        self.time_park = time_park

    def drive_go(self,time_go):
        self.time_go = time_go

    def drive_leave(self,time_leave):
        self.time_leave = time_leave

