from typing   import Callable, Optional
from io       import TextIOBase

from .auxiliary import Filler
from .gradient  import Gradient


class JLog:

    _init_is_useless = False
    _color_init_ok   = False

    def __init__(
            self,
            *buffers:      TextIOBase,
            offset_size:   int = 2,
            offset_filler: Callable[[int, int], str] = Filler.whitespace,
            line_term:     str = '\r\n'
        ) -> None: ...

    def offset(self, amount: int = 1) -> None: ...
    def save_offset(self) -> None: ...
    def restore_offset(self) -> None: ...

    def string(
            self,
            *values:       object,
            offset_once:   bool               = False,
            offset_after:  int                = 0,
            fore_gradient: Optional[Gradient] = None,
            back_gradient: Optional[Gradient] = None
        ) -> None: ...
    def gap(self, size: int = 1) -> None: ...
    def divider(
            self,
            sequence:     str = '=',
            width:        int = 25,
            margin_above: int = 0,
            margin_below: int = 1
        ) -> None: ...
    def reset_colors(self, fore: bool = True, back: bool = True) -> None: ...
    def close_all(self, ignore_ttys: bool = True) -> None: ...