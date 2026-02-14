'''
> Me: Can we stop and get some `lolcat`?  
> Mom: We have `lolcat` at home  
> `lolcat` at home:
'''


class ColorPoint:
    '''
    An anchor point of the gradient.
    '''

    def __init__(self, r: int, g: int, b: int, pos: float) -> None:
        '''
        Define an anchor point of the gradient.

        Args:
            r (int): red component of the color.
            g (int): green component of the color.
            b (int): blue component of the color.
            pos (float): a position of the anchor point. Recommended: 0.0 <= pos <= 1.0.

        Raises:
            ValueError: raised if one or many color components are invalid (`not in range(0, 256)`).
        '''

        if not (0 <= r <= 255) or not (0 <= g <= 255) or not (0 <= b <= 255):
            raise ValueError('color components cannot be lesser than 0 or greater than 255')

        self.r   = r
        self.g   = g
        self.b   = b
        self.pos = pos

    @property
    def color_tuple(self) -> tuple[int, int, int]:
        '''
        `(r, g, b)` tuple.
        '''
        return self.r, self.g, self.b


class Gradient:
    '''
    A gradient class. That's it.
    '''

    def __init__(self, *points: ColorPoint) -> None:
        '''
        Creates a new gradent.

        Raises:
            ValueError: raised if no points are passed.
        '''

        if not points:
            raise ValueError('gradient should contain at least one ColorPoint')
        
        points = tuple(sorted(points, key = lambda x: x.pos))
        self._points: list[ColorPoint] = []

        for idx in range(len(points) - 1):
            if points[idx].pos != points[idx + 1].pos:
                self._points.append(points[idx])
        self._points.append(points[-1])

    @property
    def points(self) -> list[ColorPoint]:
        '''
        The list of all anchor points of this gradient.
        '''

        return self._points

    def get_color_in_position(self, pos: float) -> tuple[int, int, int]:
        '''
        Calculates and returns a color in any position of the gradient.

        Args:
            pos (float): target position.
        '''

        lr: tuple[list[ColorPoint], list[ColorPoint]] = ([], [])

        for point in self.points:
            if point.pos < pos:
                lr[0].append(point)
                continue
            if point.pos > pos:
                lr[1].append(point)
                continue
            return point.color_tuple
        
        if not lr[0]:
            return lr[1][0].color_tuple
        left = lr[0][-1]

        if not lr[1]:
            return lr[0][-1].color_tuple
        right = lr[1][0]

        return (
            round(left.r + (right.r - left.r) / (right.pos - left.pos) * (pos - left.pos)),
            round(left.g + (right.g - left.g) / (right.pos - left.pos) * (pos - left.pos)),
            round(left.b + (right.b - left.b) / (right.pos - left.pos) * (pos - left.pos))
        )