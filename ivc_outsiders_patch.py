"""

"""
import configparser
from submodules.python_core_libs.logging.project_logger import Log
import os
from shutil import copyfile


def read_file_lines(file_path):
    with open(file_path) as f:
        return f.readlines()


def write_file_lines(file_path, lines):
    with open(file_path, 'w') as f:
        f.writelines(lines)


def replace_outsider(lines):
    logger = Log.instance().logger
    for i, line in enumerate(lines):
        l: str = line
        res = l.find("outsiders")
        if res != -1:
            logger.info(f"Replacing '{line[:-1]}' with 'outsiders = all' in file")
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
    logger = Log.instance().logger
    if not os.path.isfile(client_ini_path_bkp):
        logger.info(f"Creating backup-file {client_ini_path_bkp}")
        copyfile(client_ini_path, client_ini_path_bkp)
    else:
        logger.info(f"Skipping creation of backup-file {client_ini_path_bkp} as it already exists.")


def create_logger_ini():
    logger_ini_content = """[formatters]
keys=default

[formatter_default]
format=<%(levelname)-3s><%(asctime)s> %(message)s <%(filename)s:%(lineno)d>'
class=logging.Formatter

[handlers]
keys=console, file

[handler_console]
class=logging.StreamHandler
formatter=default
args=tuple()

[handler_file]
class=logging.FileHandler
level=INFO
formatter=default
args=("ivc_outsiders_patch.log", "w")

[loggers]
keys=root

[logger_root]
level=INFO
formatter=default
handlers=console,file"""

    ini_exists: bool = os.path.isfile("ivc_outsiders_patch_logger.ini")
    if not ini_exists:
        with open("ivc_outsiders_patch_logger.ini", 'w') as f:
            f.write(logger_ini_content)


def remove_logger_ini():
    ini_exists: bool = os.path.isfile("ivc_outsiders_patch_logger.ini")
    if ini_exists:
        os.remove("ivc_outsiders_patch_logger.ini")


if __name__ == "__main__":
    create_logger_ini()
    logger = Log.instance().logger
    Log.instance().set_ini("ivc_outsiders_patch_logger.ini")
    logger.info("Start")
    Log.instance().set_ini("ivc_outsiders_patch_logger.ini")
    main()

    remove_logger_ini()

