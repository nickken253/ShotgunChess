class Line:
    def __init__(self, color=(0, 0, 0), start_pos=(0, 0), end_pos=(0, 0), thickness=1):
        self.color = color
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.thickness = thickness

    def render(self):
        from pygame import draw
        from gamemanager import WConnect
        draw.line(WConnect.window, self.color, self.start_pos, self.end_pos, self.thickness)


class Curve:
    def __init__(self, color=(0, 0, 0), points=None, thickness=1, closed=False):
        if points is None:
            points = []
        self.color = color
        self.points = points
        self.thickness = thickness
        self.closed = closed

    def render(self):
        from pygame import draw
        from gamemanager import WConnect
        draw.lines(WConnect.window, self.color, self.closed, self.points, self.thickness)
