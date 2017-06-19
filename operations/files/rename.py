import os


class Rename:
    @staticmethod
    def walker(recursive, original_name, original_extension, new_name, new_extension, rootdir):
        # pass through every file and directory
        for path, dirs, files in os.walk(rootdir):
            # for each direct subdirectory...
            if recursive:
                for folder in dirs:
                    # call the walker
                    Rename.walker(recursive,
                                  original_name,
                                  original_extension,
                                  new_name,
                                  new_extension,
                                  os.path.join(path, folder))
            # pass through every file and directory
            for p, d, f in os.walk(path):
                # for each file...
                for name in f:
                    if original_name == '*':
                        if name.endswith('.' + original_extension):
                            # print(relative_file)
                            relative_file = os.path.join(path, name)
                            new_relative_file = os.path.join(path, new_name + '.' + new_extension)
                            os.rename(relative_file, new_relative_file)
                    else:
                        if name == original_name + '.' + original_extension:
                            # print(relative_file)
                            relative_file = os.path.join(path, name)
                            new_relative_file = os.path.join(path, new_name + '.' + new_extension)
                            os.rename(relative_file, new_relative_file)

    @staticmethod
    def run(is_recursive, original_name, original_extension, new_name, new_extension, rootdir=os.getcwd()):
        Rename.walker(is_recursive,
                      original_name,
                      original_extension,
                      new_name,
                      new_extension,
                      rootdir)