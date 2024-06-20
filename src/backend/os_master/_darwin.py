from os.path import expanduser, join

from src.backend.os_master._interface import AbstractOSMaster


class DarwinMaster(AbstractOSMaster):
    name = "darwin"
    hosts_path = "/etc/hosts"
    hosts_folder = "/etc"
    user_folder = join(expanduser("~"), "hosts_backups")
