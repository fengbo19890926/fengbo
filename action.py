'''测试结果'''
from owner import Owner
from car import Car
from parking_place import Parking_place
from parking_info import Parking_info
from position import Position
from order import Order

'''实例化各个对象'''
car = Car('辽E88888','奥迪A7')
owner = Owner('冯博',car)
position = Position(2,'C3-17')
info = Parking_info(owner,car,position)
owner.drive_in('2018-11-26 11:30:00')  
order = Order(info)
parking_place = Parking_place(order)
owner.drive_park('2018-11-26 11:32:00')
Parking_place.positions[22] = position
'''把车位信息更改为已占用'''
position.set_occupied()
owner.drive_go('2018-11-26 12:28:00')
'''把车位信息更改为已占用可用'''
position.set_empty()
owner.drive_leave('2018-11-26 12:30:00')
parking_place.print_order()
