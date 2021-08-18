
class grant:
    def everything(self, selector:str = '@s'):
        return f'advancement grant {selector} everything'

    def from_advancement(self, advancement: str, selector:str = '@s'):
        return f'advancement grant {selector} from {advancement}'

    def only(self, advancement: str, selector:str = '@s'):
        return f'advancement grant {selector} only {advancement}'

    def through(self, advancement: str, selector:str = '@s'):
        return f'advancement grant {selector} through {advancement}'

    def until(self, advancement: str, selector:str = '@s'):
        return f'advancement grant {selector} until {advancement}'

class revoke:
    def everything(self, selector:str = '@s'):
        return f'advancement revoke {selector} everything'

    def from_advancement(self, advancement: str, selector:str = '@s'):
        return f'advancement revoke {selector} from {advancement}'

    def only(self, advancement: str, selector:str = '@s'):
        return f'advancement revoke {selector} only {advancement}'

    def through(self, advancement: str, selector:str = '@s'):
        return f'advancement revoke {selector} through {advancement}'

    def until(self, advancement: str, selector:str = '@s'):
        return f'advancement revoke {selector} until {advancement}'