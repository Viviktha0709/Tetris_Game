class Colors:
    dark_grey = (25, 30, 40)
    green = (50, 230, 20)
    red = (230, 20, 20)
    orange = (225, 120, 20)
    yellow = (240, 235, 5)
    purple = (170, 0, 250)
    cyan = (20, 200, 210)
    blue = (10, 60, 220)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (92, 131, 191)


    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
