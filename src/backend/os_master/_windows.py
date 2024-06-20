from os.path import expanduser, join

from src.backend.os_master._interface import AbstractOSMaster


class WindowsMaster(AbstractOSMaster):
    name = "windows"
    hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    hosts_folder = "C:\\Windows\\System32\\drivers\\etc"
    user_folder = join(expanduser("~"), "hosts_backup")
