import os
import random
import ctypes


class SetIcon:
    @staticmethod
    def walker(rootdir):
        # pass through every file and directory
        for path, dirs, files in os.walk(rootdir):
            # for each direct subdirectory...
            for folder in dirs:
                # call the walker
                SetIcon.walker(os.path.join(path, folder))
                # initialize icon list
                icons = list()
                # pass through every file and directory
                for p, d, f in os.walk(os.path.join(path, folder)):
                    # for each file...
                    for name in f:
                        # if it is an icon...
                        if ".ico" in name:
                            # construct its relative path...
                            relative_dir = os.path.relpath(p, os.path.join(path, folder))
                            relative_file = os.path.join(relative_dir, name)
                            # and add it to the list
                            icons.append(relative_file)
                # if the list is not empty...
                if icons:
                    # select a random icon...
                    icon = random.choice(icons)
                    # and (try to) create the Desktop.ini file
                    try:
                        # open file and write to it
                        with open(os.path.join(path, folder, "Desktop.ini"), 'w') as folder_settings:
                            folder_settings.write("[.ShellClassInfo]\nIconFile=" + icon + "\nIconIndex=0")
                        # set Desktop.ini as hidden
                        ctypes.windll.kernel32.SetFileAttributesW(os.path.join(path, folder, "Desktop.ini"))
                        # set current directory as a system directory (needed to make Desktop.ini work)
                        # ctypes.windll.kernel32.SetFileAttributesW(os.path.join(path, folder), 128) //4
                        # set Desktop.ini as a system file
                        # ctypes.windll.kernel32.SetFileAttributesW(os.path.join(path, folder, "Desktop.ini"), 4)
                    # if it doesn't succeed...
                    except PermissionError:
                        # welp.
                        pass

    @staticmethod
    def run(rootdir=os.getcwd()):
        SetIcon.walker(rootdir)
