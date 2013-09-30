import sfml as sf


class Moving:
    def movupdate(self):
        """
        simple movement here
        @return: MovingRect
        """
        if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
            self.position += (5, 0)
        if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
            self.position -= (5, 0)
        if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
            self.position -= (0, 5)
        if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
            self.position += (0, 5)
        return self


class Rectan(Moving, sf.RectangleShape):
    def __init__(self):
        super(Rectan, self).__init__()


class Circle(Moving, sf.CircleShape):
    def __init__(self):
        super(Circle, self).__init__()


