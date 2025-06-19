class ManualComment:

    def __init__(self, x: str, y: str) -> None:
        self.x = x
        self.y = y


    def get_x(self)->None:
        return self.x

    def get_y(self)->None:
        return self.y

    def __eq__(self, other):
        if isinstance(self.__class__, other.__class__):
            return True
        else:
            return False
        

ommen = ManualComment("1", "1")
