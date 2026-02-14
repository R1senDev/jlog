from typing   import Callable, Literal, Optional
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

    def _pop_colors(self, string: str) -> str: ...
    def _gradientify(
            self,
            string: str,
            fore_gradient: Optional[Gradient] = None,
            back_gradient: Optional[Gradient] = None
        ) -> str: ...
    def _do_subs(
            self,
            string: str,
            colors: bool = True
        ) -> str: ...
    def _cast(
            self,
            string:   str,
            nl:       bool = True,
            do_subs:  Literal['no', 'tty', 'everywhere'] = 'tty',
            tty_only: bool = False,
            skip_tty: bool = False
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