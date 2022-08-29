from munch import DefaultMunch

class System:
    
    @staticmethod
    def get_CPU() -> DefaultMunch:
        ...
        info = dict()
        return DefaultMunch.fromDict(info)
    
    @staticmethod
    def get_GPU() -> DefaultMunch:
        ...
        info = dict()
        return DefaultMunch.fromDict(info)
    
    @staticmethod
    def get_RAM() -> DefaultMunch:
        ...
        info = dict()
        return DefaultMunch.fromDict(info)
    
    @staticmethod
    def get_ROM() -> DefaultMunch:
        ...
        info = dict()
        return DefaultMunch.fromDict(info)

