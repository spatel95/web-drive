import json

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]



class Config(metaclass=Singleton):
    _instance = None
    def __init__(self):
        self.DRIVE_DIR = "/tmp/"
        self.REDIRECT_URL = "/drive/"    

    def __getattr__(self, item):
        return self[item]

    def __dir__(self):
        return super().__dir__() + [str(k) for k in self.keys()]

        
    def get_config_json(self):
        return json.dumps(self.__dict__)
    
