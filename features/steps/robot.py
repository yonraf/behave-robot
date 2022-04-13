class Robot:
    def __init__(self):
         self.controller = None
         self.receiver = None
         self.io = None
      
    # getter method
    def get_controller(self):
        return self._controller
      
    # setter method
    def set_controller(self, controller):
        self._controller = controller

    # getter method
    def get_receiver(self):
        return self._receiver
      
    # setter method
    def set_receiver(self, receiver):
        self._receiver = receiver

    # getter method
    def get_io(self):
        return self._io
      
    # setter method
    def set_io(self, io):
        self._io = io
