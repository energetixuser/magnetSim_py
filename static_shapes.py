import sfml as sf
class MovingRect (sf.RectangleShape):
    def rectupdate(self):
        if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
            self.position += (5, 0)
        elif sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
            self.position -= (5, 0)
        elif sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
            self.position -= (0, 5)
        elif sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
            self.position += (0, 5)
        return self