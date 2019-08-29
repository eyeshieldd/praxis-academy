
class EmailClient(object):
    
    def __init__(self, config):
        self._config = config
        self.connect(self._config)
        
    def connect(self, config):
        # Implement function here
        pass