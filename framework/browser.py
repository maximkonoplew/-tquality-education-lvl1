from framework.singleton import Singleton 

class Browser(Singleton):
    driver = {}
    
    def __init__(self):
        super().__init__()