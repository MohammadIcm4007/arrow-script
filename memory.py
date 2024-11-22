class memory:
    def __init__(self):
        self.memory_view = {}

    def set(self, key, value):
        self.memory_view[key] = value

    def get(self, key):
        return self.memory_view[key]
