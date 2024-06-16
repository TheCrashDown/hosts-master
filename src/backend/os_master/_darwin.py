from src.backend.os_master._interface import AbstractOSMaster


class DarwinMaster(AbstractOSMaster):
    name = "darwin"
    hosts_path = "/etc/hosts"
    backup_folder = "/etc"
