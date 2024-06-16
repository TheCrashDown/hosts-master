from abc import ABC


class AbstractOSMaster(ABC):
    name: str
    hosts_path: str
    backup_folder: str
