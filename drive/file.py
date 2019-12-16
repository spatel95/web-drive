
class File():
    def __init__(self, name, size, creation_date, mod):
        self.name = name
        self.size = size
        self.creation_date = creation_date
        self.mod_date = mod
        # TODO add SHA256 Hash too

    def serialize(self):
        return {
            'name': self.name,
            'size': self.size,
            'creation_date': self.creation_date,
            'mod_date': self.mod_date
        }