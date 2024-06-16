from src.backend.os_master._interface import AbstractOSMaster


class LinuxMaster(AbstractOSMaster):
    name = "linux"
    hosts_path = "/etc/hosts"
    backup_folder = "/etc"
