import configparser

class Settings():
    
    def __init__(self, file):
        self._settingsfile = file
        self._config = configparser.RawConfigParser()
        self._config.read(file)
    
    def get_sections(self):
        return self._config.sections()
    
    def get_dimension(self):
        return self._config.get("DIMENSION", "dimension")

    def get_apples(self):
        return self._config.get("APPLES", "apples")