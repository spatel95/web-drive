from os import listdir


class DriveFiles:
    def __init__(self, root_dir):
        self._root_dir = root_dir

    def list_file(self, user, dir_loc):
        return str(listdir(self._root_dir+dir_loc))
