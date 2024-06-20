from abc import ABC


class AbstractOSMaster(ABC):
    name: str
    hosts_path: str
    hosts_folder: str
    user_folder: str
