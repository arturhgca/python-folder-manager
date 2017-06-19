import os


class AssertRules:
    @staticmethod
    def walker(rootdir, target_files):
        # pass through every file and directory
        for path, dirs, files in os.walk(rootdir):
            # for each direct subdirectory...
            noncompliant_folders = list()
            for folder in dirs:
                # call the walker
                AssertRules.walker(os.path.join(path, folder))
                # pass through every file and directory
                for p, d, f in os.walk(os.path.join(path, folder)):
                    # for each file...
                    for target in target_files:
                        found_target = False
                        for name in f:
                            if target in name:
                                found_target = True
                                break
                        if not found_target:
                            noncompliant_folders.append(p)
                            break
            # if the list is not empty...
            if noncompliant_folders:
                for folder in noncompliant_folders:
                    print(folder)

    @staticmethod
    def run(target_files, rootdir=os.getcwd()):
        AssertRules.walker(rootdir, target_files)