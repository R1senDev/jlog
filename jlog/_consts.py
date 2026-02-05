COLOR_RESET_FORE = '\033[39m'
COLOR_RESET_BACK = '\033[49m'

# Base+EGA palette
COLORS_SCHEME_BASE = [
    # Normal foreground colors
    (r'\[jl:fg:black\]',   '\033[30m'),
    (r'\[jl:fg:red\]',     '\033[31m'),
    (r'\[jl:fg:green\]',   '\033[32m'),
    (r'\[jl:fg:yellow\]',  '\033[33m'),
    (r'\[jl:fg:blue\]',    '\033[34m'),
    (r'\[jl:fg:magenta\]', '\033[35m'),
    (r'\[jl:fg:cyan\]',    '\033[36m'),
    (r'\[jl:fg:white\]',   '\033[37m'),

    # Bright foreground colors
    (r'\[jl:fg:bblack\]',   '\033[90m'),
    (r'\[jl:fg:bred\]',     '\033[91m'),
    (r'\[jl:fg:bgreen\]',   '\033[92m'),
    (r'\[jl:fg:byellow\]',  '\033[93m'),
    (r'\[jl:fg:bblue\]',    '\033[94m'),
    (r'\[jl:fg:bmagenta\]', '\033[95m'),
    (r'\[jl:fg:bcyan\]',    '\033[96m'),
    (r'\[jl:fg:bwhite\]',   '\033[97m'),

    # Normal background colors
    (r'\[jl:bg:black\]',   '\033[40m'),
    (r'\[jl:bg:red\]',     '\033[41m'),
    (r'\[jl:bg:green\]',   '\033[42m'),
    (r'\[jl:bg:yellow\]',  '\033[43m'),
    (r'\[jl:bg:blue\]',    '\033[44m'),
    (r'\[jl:bg:magenta\]', '\033[45m'),
    (r'\[jl:bg:cyan\]',    '\033[46m'),
    (r'\[jl:bg:white\]',   '\033[47m'),

    # Bright background colors
    (r'\[jl:bg:bblack\]',   '\033[100m'),
    (r'\[jl:bg:bred\]',     '\033[101m'),
    (r'\[jl:bg:bgreen\]',   '\033[102m'),
    (r'\[jl:bg:byellow\]',  '\033[103m'),
    (r'\[jl:bg:bblue\]',    '\033[104m'),
    (r'\[jl:bg:bmagenta\]', '\033[105m'),
    (r'\[jl:bg:bcyan\]',    '\033[106m'),
    (r'\[jl:bg:bwhite\]',   '\033[107m'),

    # Reset
    (r'\[jl:fg:rst\]', COLOR_RESET_FORE),
    (r'\[jl:bg:rst\]', COLOR_RESET_BACK),
    (r'\[jl:rst\]',    '\033[0m')
]

# 256-bit palette
COLORS_SCHEME_256B = [
    (r'\[jl:fg:(?P<value>\d{1,3})\]', r'\033[38;5;\g<value>m'), # foreground
    (r'\[jl:bg:(?P<value>\d{1,3})\]', r'\033[48;5;\g<value>m'), # background
]

# TrueColor palette
COLORS_SCHEME_TRCL = [
    (r'\[jl:fg:(?P<r>\d{1,3}),(?P<g>\d{1,3}),(?P<b>\d{1,3})\]', r'\033[38;2;\g<r>;\g<g>;\g<b>m'), # foreground
    (r'\[jl:bg:(?P<r>\d{1,3}),(?P<g>\d{1,3}),(?P<b>\d{1,3})\]', r'\033[48;2;\g<r>;\g<g>;\g<b>m')  # background
]