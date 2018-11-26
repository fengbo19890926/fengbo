class Order():
    def __init__(self,parking_info):
        self.parking_info = parking_info
# 计算花费
    def cost(self):
        return self.parking_info.time_duration()/60*0.2*(self.parking_info.position.level)
    
        

