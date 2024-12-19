class Singleton:
    __instance = {}

    def __new__(cls):
        if cls.__instance == {}:
            cls.__instance = super().__new__(cls)
        return cls.__instance