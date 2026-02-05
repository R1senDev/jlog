def info() -> None:
    from random import choice
    from sys    import stdout
    from io     import TextIOBase

    from .gradient import Gradient, ColorPoint
    from .logger   import JLog

    if not isinstance(stdout, TextIOBase):
        exit(0)

    gradient = choice([
        Gradient(
            ColorPoint(255, 0, 0, 0.0),
            ColorPoint(255, 128, 0, 1.0)
        ),
        Gradient(
            ColorPoint(0, 255, 0, 0.0),
            ColorPoint(0, 204, 255, 1.0)
        ),
        Gradient(
            ColorPoint(255, 0, 255, 0.0),
            ColorPoint(255, 0, 0, 1.0)
        ),
        Gradient(
            ColorPoint(255, 0, 0, 1.0),
            ColorPoint(255, 128, 0, 0.0)
        ),
        Gradient(
            ColorPoint(0, 255, 0, 1.0),
            ColorPoint(0, 204, 255, 0.0)
        ),
        Gradient(
            ColorPoint(255, 0, 255, 1.0),
            ColorPoint(255, 0, 0, 0.0)
        ),
    ])

    jl = JLog(stdout)

    jl.gap()
    jl.string(
        f'JLog v0.1.0 by R1senDev',
        fore_gradient = gradient
    )
    jl.string('A lightweight, colorful logging library with gradient text support and hierarchical offsetting.')
    jl.divider(margin_top = 1)
    jl.string('Features:')
    jl.offset(+1)
    jl.string('[jl:fg:cyan]•[jl:fg:rst] Hierarchical offset system for structured logs')
    jl.string('[jl:fg:cyan]•[jl:fg:rst] TrueColor gradients & 256-color palette support')
    jl.string('[jl:fg:cyan]•[jl:fg:rst] Custom tags [jl:fg:byellow][jl:bg:blue]for coloring[jl:rst]')
    jl.string('[jl:fg:cyan]•[jl:fg:rst] Multi-output streams (files, stdout, stderr)')
    jl.string('[jl:fg:cyan]•[jl:fg:rst] Dividers, gaps, and visual separation tools')
    jl.offset(-1)
    jl.string('Perfect for CLI apps, debug output, and making logs actually readable!')
    jl.divider(margin_top = 1)
    jl.string('GitHub: https://github.com/R1senDev/jlog')
    jl.string('Have fun! :D')