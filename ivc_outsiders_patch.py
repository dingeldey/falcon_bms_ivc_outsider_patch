"""

"""
import configparser
import os.path
import traceback
import re
from submodules.python_core_libs.logging.project_logger import Log


def read_file_lines(file_path):
    with open(file_path) as f:
        return f.readlines()


def write_file_lines(file_path, lines):
    with open(file_path, 'w') as f:
        f.writelines(lines)


def replace_outsider(lines):
    logger = Log.instance().logger
    logger.info("Parsing")
    for i, line in enumerate(lines):
        l: str = line
        res = l.find("outsiders")
        if res != -1:
            lines[i] = "outsiders = all\n"


def main():
    import os.path
    ini_exists: bool = os.path.isfile("config.ini")

    bms_path = "./"
    if ini_exists:
        bms_path = get_ini_entries()

    logger = Log.instance().logger
    client_ini_path = os.path.join(bms_path, "Bin/x64/IVC/IVC Client.ini")
    client_ini_path_bkp = os.path.join(bms_path, "Bin/x64/IVC/IVC Client_backup.ini")
    work_on_ini(client_ini_path, client_ini_path_bkp, logger)

    client_ini_path = os.path.join(bms_path, "Bin/x86/IVC/IVC Client.ini")
    client_ini_path_bkp = os.path.join(bms_path, "Bin/x86/IVC/IVC Client_backup.ini")
    work_on_ini(client_ini_path, client_ini_path_bkp, logger)


def get_ini_entries():
    cfg_ini = configparser.ConfigParser()
    cfg_ini.read("config.ini")
    bms_path: str = cfg_ini["BMS"]["bmsFolder"]
    return bms_path


def work_on_ini(client_ini_path, client_ini_path_bkp, logger):
    logger.info(f"Starting to work in file {client_ini_path}")
    make_ini_backup(client_ini_path, client_ini_path_bkp)
    ini_lines = read_file_lines(client_ini_path)
    replace_outsider(ini_lines)
    write_file_lines(client_ini_path, ini_lines)


def make_ini_backup(client_ini_path, client_ini_path_bkp):
    from shutil import copyfile
    copyfile(client_ini_path, client_ini_path_bkp)


if __name__ == "__main__":
    main()
    Log.instance().set_ini("logger.ini")
