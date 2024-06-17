import os
from datetime import datetime

from src.backend.file import HostsFileHelper as HostsFileHelper
from src.backend.os_master import OSMaster as OSMaster


class HostsManager:
    os_master: OSMaster
    file_content: list[str]

    def __init__(self) -> None:
        self.os_master = OSMaster()

    def get_hosts(self) -> None:
        try:
            self.file_content = HostsFileHelper.read_hosts(self.os_master.hosts_path)
        except Exception:
            # TODO: handle error
            raise

    def set_hosts(self) -> None:
        try:
            HostsFileHelper.write_hosts(self.os_master.hosts_path, self.file_content)
        except Exception:
            # TODO: handle error
            raise

    def get_backup_name(self) -> str:
        name = f"hosts_{int(datetime.now().timestamp())}.bak"
        return os.path.join(self.os_master.backup_folder, name)

    def backup_hosts(self) -> None:
        try:
            HostsFileHelper.write_hosts(self.get_backup_name(), self.file_content)
        except Exception:
            # TODO: handle error
            raise
