from colorama import init
from typing   import TextIO, Callable, Literal, Optional
from string   import whitespace
from re       import sub

from .auxiliary import Filler
from .gradient  import Gradient
from ._consts   import COLORS_SCHEME_BASE, COLORS_SCHEME_256B, COLORS_SCHEME_TRCL, COLOR_RESET_FORE, COLOR_RESET_BACK


class JLog:

    _init_is_useless = False
    _color_init_ok   = False

    def __init__(
            self,
            *buffers:      TextIO,
            offset_size:   int = 2,
            offset_filler: Callable[[int, int], str] = Filler.whitespace,
            line_term:     str = '\r\n'
        ) -> None:

        queued_messages: list[str] = []

        self._buffers          = buffers
        self._offset_generator = offset_filler
        self._offset_size      = offset_size
        self._line_term        = line_term

        self.current_offset = 0
        
        if not JLog._init_is_useless:
            try:
                init()
                JLog._color_init_ok = True
            except Exception as exc:
                queued_messages.append(f'Unable to initialize colored output: {exc.__class__.__name__}: {exc}')
            JLog._init_is_useless = True

        if queued_messages:
            self.string('[jl:fg:byellow]There are errors occurred during JLog initialization:[jl:fg:rst]')
            self.offset(+1)
            for message in queued_messages:
                self.string(message)
            self.offset(-1)
            self.gap()

    def _pop_colors(self, string: str) -> str:
        new_string = string
        for key, _ in COLORS_SCHEME_BASE + COLORS_SCHEME_256B + COLORS_SCHEME_TRCL:
            new_string = sub(key, '', new_string)
        return new_string
    
    def _gradientify(
            self,
            string: str,
            fore_gradient: Optional[Gradient] = None,
            back_gradient: Optional[Gradient] = None
        ) -> str:
        if fore_gradient is None and back_gradient is None:
            return string

        new_string = self._pop_colors(string)
        base = new_string

        if not (base and base.isprintable()):
            return string

        prefix = ''
        for char in new_string:
            if char in whitespace:
                prefix += char
                base = base[1:]
                continue
            break
        suffix = ''
        for char in reversed(new_string):
            if char in whitespace:
                suffix = char + suffix
                base = base[:-1]
                continue
            break

        new_string = prefix

        for idx, char in enumerate(base):
            if fore_gradient:
                color = fore_gradient.get_color_in_position(idx / len(base))
                new_string += f'\033[38;2;{";".join(map(str, color))}m'
            if back_gradient:
                color = back_gradient.get_color_in_position(idx / len(base))
                new_string += f'\033[48;2;{";".join(map(str, color))}m'
            new_string += char
        
        return new_string + COLOR_RESET_FORE + COLOR_RESET_BACK + suffix

    def _do_subs(
            self,
            string: str,
            colors: bool = True
        ) -> str:
        new_string = string

        if JLog._color_init_ok and colors:
            for pair in COLORS_SCHEME_BASE + COLORS_SCHEME_256B + COLORS_SCHEME_TRCL:
                new_string = sub(*pair, new_string)
        else:
            return self._pop_colors(string)

        return new_string

    def _cast(
            self,
            string:   str,
            nl:       bool = True,
            do_subs:  Literal['no', 'tty', 'everywhere'] = 'tty',
            tty_only: bool = False,
            skip_tty: bool = False
        ) -> None:

        if tty_only and skip_tty:
            self.string('[jl:fg:byellow]tty_only == skip_tty == True. The selector does not cover anything.[jl:fg:rst]', offset_once = True)
            return

        for buffer in self._buffers:

            if buffer.closed or (skip_tty and buffer.isatty()) or (tty_only and not buffer.isatty()):
                continue

            if do_subs == 'everywhere' or (do_subs == 'tty' and buffer.isatty()):
                buffer.write(self._do_subs(string) + self._line_term * nl)
                continue
            buffer.write(self._do_subs(string, colors = False) + self._line_term * nl)
            buffer.flush()

    def offset(self, amount: int = 1) -> None:
        '''
        Changes current offset of the output.

        Args:
            amount (int, optional): amount of the offset units to add. Defaults to 1.

        Examples:
            ```python
            jl = jlog.JLog(sys.stdout)
            jl.string('Initializing...')
            jl.offset(+1)
            jl.string('Loading config')
            jl.string('Loading meta')
            jl.string('Loading scripts')
            jl.offset(-1)
            jl.string('All set!')
            ```
        '''
        self.current_offset += amount

    def string(
            self,
            *values:       object,
            offset_once:   bool = False,
            fore_gradient: Optional[Gradient] = None,
            back_gradient: Optional[Gradient] = None
        ) -> None:
        '''
        Outputs a single line.

        Args:
            offset_once (bool, optional): temporarily adds a single offset unit to the output. Defaults to False.

        Examples:
            ```python
            jl = jlog.JLog(sys.stdout)
            jl.string('Hello, World!')
            ```
        '''

        string = self._offset_generator(self.current_offset + offset_once, self._offset_size) + ''.join(map(str, values))

        string = self._gradientify(
            string,
            fore_gradient = fore_gradient,
            back_gradient = back_gradient
        )

        self._cast(string)
    
    def gap(self, size: int = 1) -> None:
        '''
        Outputs a vertical gap.

        Args:
            size (int, optional): number of the lines to skip. Defaults to 1.

        Examples:
            ```python
            jl = jlog.JLog(sys.stdout)
            jl.string('Restart!')
            jl.gap()
            jl.string('Initializing...')
            ```
        '''
        self._cast(self._line_term * size, False)

    def divider(
            self,
            sequence:      str = '=',
            width:         int = 25,
            margin_top:    int = 0,
            margin_bottom: int = 1
        ) -> None:
        divider = ''.join(sequence[i % len(sequence)] for i in range(width))
        self.gap(margin_top)
        self.string(divider)
        self.gap(margin_bottom)

    def reset_colors(self, fore: bool = True, back: bool = True) -> None:
        if not JLog._color_init_ok:
            return
        
        string = ''
        if fore:
            string += COLOR_RESET_FORE
        if back:
            string += COLOR_RESET_BACK
        
        self._cast(string, nl = True, do_subs = 'no', tty_only = True)

    def close_all(self, ignore_ttys: bool = True) -> None:
        for buffer in self._buffers:
            if buffer.isatty() and ignore_ttys:
                continue
            buffer.close()