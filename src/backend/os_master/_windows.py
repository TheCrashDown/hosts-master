from src.backend.os_master._interface import AbstractOSMaster


class WindowsMaster(AbstractOSMaster):
    name = "windows"
    hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    backup_folder = "C:\\Windows\\System32\\drivers\\etc"
