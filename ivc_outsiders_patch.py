"""

"""
import os.path
import traceback
import re


def read_file_lines(file_path):
    with open(file_path) as f:
        return f.readlines()

def replace_outsider(lines):



def main():
    cwd_path = os.getcwd()
    client_ini_path = os.path.join(cwd_path, "Bin/x64/IVC/IVC Client.ini")
    client_ini_path_bkp = os.path.join(cwd_path, "Bin/x64/IVC/IVC Client_backup.ini")

    make_ini_backup(client_ini_path, client_ini_path_bkp)
    ini_lines = read_file_lines(client_ini_path)
    replace_outsider(ini_lines)



def make_ini_backup(client_ini_path, client_ini_path_bkp):
    from shutil import copyfile
    copyfile(client_ini_path, client_ini_path_bkp)


if __name__ == "__main__":
    main()
