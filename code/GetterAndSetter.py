class car:
    def __init__(self,a=40):
        self._speed=a #this _speed undescore made the python program or that part private show accessible by getter and setter only
    def get_speed(self):
        return self.speed
    def set_speed(self,a):
        self._speed=a
        return
"""
>>> c1=car()
>>> c1.get_speed()
40
>>> c1.set_speed(60)
>>> c1.get_speed()
60
"""
