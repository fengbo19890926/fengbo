'''停车场类'''
from position import Position
class Parking_place():
    # 初始化车位
    positions = []
    for x in range(0,10):
        positions.append(Position(1))
    for x in range(10,20):
        positions.append(Position(2))
    for x in range(20,30):
        positions.append(Position(3))
    
    def __init__(self,order):
        self.order = order

# 获取车位数量
    def get_position_count(self): 
        count = 0
        for x in Parking_place.positions:
            count = count+x.status
        return 30-count

# 打印订单
    def print_order(self):
        print("尊敬的"+str(self.order.parking_info.owner.name))
        print("您的车："+str(self.order.parking_info.car.car_id))
        print("停车位为："+str(self.order.parking_info.position.position_num))
        print("停留时间为"+str(self.order.parking_info.time_duration()/3600)+"小时")
        print("共计消费："+str(self.order.cost())+"元")


