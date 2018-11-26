class Position():
    def __init__(self,level,status=0,position_num=""):
        self.level = level
        self.status = status
        self.position_num = position_num

    def set_occupied(self):
        self.status = 1
    def set_empty(self):
        self.status = 0


 