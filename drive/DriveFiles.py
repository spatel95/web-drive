from os import listdir, stat
from .file import File as DriveFile

class DriveFiles:
    def __init__(self, root_dir):
        self._root_dir = root_dir

    def list_file(self, user, dir_loc):
        file_list = []
        base_dir = self._root_dir+dir_loc
        for file in listdir(base_dir):
            print(file)
            stinfo = stat(base_dir+"/"+file)
            file_list.append(DriveFile(file, stinfo.st_size, stinfo.st_ctime, stinfo.st_mtime))

        print(file_list)
        return file_list
        # return str(listdir(self._root_dir+dir_loc))
