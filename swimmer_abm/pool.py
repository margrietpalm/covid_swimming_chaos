class Pool:
    def __init__(self, length=25):                    
        self.length = float(length)
        if self.length < 0:
            raise ValueError
        