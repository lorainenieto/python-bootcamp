
class Door:
    def __init__(self,closed= False):
        self.closed = closed

    def open(self):
        if self.closed == False:
            print("You can't open an open door")
        else:
            self.closed = False
            print("It's opened")

    def close(self):
        if self.closed == True:
            print("You can't close a closed door")
        else:
            self.closed = True
            print("It's closed")

door = Door()
door.close()
door.close()
door.open()
door.open()





