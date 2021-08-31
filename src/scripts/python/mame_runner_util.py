# Credit for change_permissions_recursive to Rajendra Dharmkar
# from https://www.tutorialspoint.com

import os
import pathlib


class MameRunnerUtil:

    @staticmethod
    def change_permissions_recursive():
        path = MameRunnerUtil.get_makefile_path()
        for root, dirs, files in os.walk(path):
            for momo in dirs:
                os.chown(os.path.join(root, momo), 777, 20)
            for momo in files:
                os.chown(os.path.join(root, momo), 777, 20)

    @staticmethod
    def get_makefile_path():
        return str(pathlib.Path().resolve()) + "/emulator/mame"

    @staticmethod
    def get_admin():
        print()