class HashList(list):
    def __hash__(self):
        return hash(str(self))
