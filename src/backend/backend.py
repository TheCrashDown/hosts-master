import os
from datetime import datetime

from src.backend.file import HostsFileHelper as HostsFileHelper
from src.backend.os_master import OSMaster as OSMaster


class HostsManagerState:
    file_content: list[str]
    backup_paths: list[str]

    def __init__(self) -> None:
        self.file_content = []
        self.backup_paths = [OSMaster.user_folder, OSMaster.hosts_folder]


class HostsManager:
    state: HostsManagerState

    def __init__(self) -> None:
        self.state = HostsManagerState(OSMaster)

    def get_hosts(self) -> None:
        try:
            self.state.file_content = HostsFileHelper.read(OSMaster.hosts_path)
        except Exception:
            # TODO: handle error
            raise

    def set_hosts(self) -> None:
        try:
            HostsFileHelper.write(OSMaster.hosts_path, self.state.file_content)
        except Exception:
            # TODO: handle error
            raise

    def get_backup_name(self) -> str:
        name = f"hosts_{int(datetime.now().timestamp())}.bak"
        return os.path.join(OSMaster.hosts_folder, name)

    def backup_hosts(self) -> None:
        try:
            HostsFileHelper.write(self.get_backup_name(), self.state.file_content)
        except Exception:
            # TODO: handle error
            raise
