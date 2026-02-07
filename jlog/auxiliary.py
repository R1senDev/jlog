class Filler:
    '''
    A class containing different fill patterns.
    '''

    @classmethod
    def whitespace(cls, offset: int, offset_size: int) -> str:
        '''
        Just the whitespaces.

        Example:
        ```
        Initializing...
            Reading configs...
                config.ini
            Reading configs done
            Fetching servers list...
        Init done in 0.67s
        ```
        '''

        return ' ' * offset_size * offset

    @classmethod
    def dash_markers(cls, offset: int, offset_size: int) -> str:
        '''
        UnorderedList-like.

        Example:
        ```
        Initializing...
          - Reading configs...
              - config.ini
          - Reading configs done
          - Fetching servers list...
        Init done in 0.67s
        ```
        '''
        
        if offset:
            return ' ' * offset_size * (offset - 1) + '-' + ' ' * (offset_size - 1)
        return ''