class Filler:

    @classmethod
    def whitespace(cls, offset: int, offset_size: int) -> str:
        return ' ' * offset_size * offset

    @classmethod
    def dash_markers(cls, offset: int, offset_size: int) -> str:
        if offset:
            return ' ' * offset_size * (offset - 1) + '-' + ' ' * (offset_size - 1)
        return ''