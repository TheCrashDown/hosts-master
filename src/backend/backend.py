import os
import re
from datetime import datetime

from src.backend.file import HostsFileHelper as HostsFileHelper
from src.backend.os_master import OSMaster as OSMaster


class HostsManagerState:
    """
    State of HostsManager
    """

    file_content: list[str]
    backup_paths: list[str]
    preferred_backup_path: str

    def __init__(self) -> None:
        self.file_content = []
        self.backup_paths = [OSMaster.user_folder, OSMaster.hosts_folder]
        self.preferred_backup_path = OSMaster.user_folder


class HostsManager:
    """
    Main backend class, managing hosts files read/write/edit/backup operations
    """

    state: HostsManagerState

    def __init__(self) -> None:
        self.state = HostsManagerState()

    def get_hosts(self) -> None:
        """
        Get current system hosts file content
        """
        try:
            self.state.file_content = HostsFileHelper.read(OSMaster.hosts_path)
        except Exception:
            # TODO: handle error
            raise

    def set_hosts(self) -> None:
        """
        Set current file content to system hosts file
        """
        try:
            HostsFileHelper.write(OSMaster.hosts_path, self.state.file_content)
        except Exception:
            # TODO: handle error
            raise

    def get_important_lines(self) -> list[tuple[int, str]]:
        """
        Get list of important lines from system hosts file

        Returns:
            list in format [(idx_in_file, line), ...]
        """
        lines = []
        for i, line in enumerate(self.state.file_content):
            if HostsFileHelper.is_line_important(line):
                lines.append(i, line)

        return lines

    def edit_line(self, idx: int, new_line: str) -> None:
        """
        Edit line in current editing file
        """
        try:
            self.state.file_content[idx] = new_line
        except Exception:
            # TODO: handle error
            raise

    def generate_backup_name(self) -> str:
        """
        Generate name for new backup file
        """
        name = f"hosts_{int(datetime.now().timestamp())}.bak"
        return name

    def get_backups_list(self) -> list[str]:
        """
        Get list of existing backup files
        """
        backups = []
        for path in self.state.backup_paths:
            if os.path.exists(path) and os.path.isdir(path):
                for file in os.listdir(path):
                    if re.match(r"hosts_[0-9]+.bak", file):
                        backups.append(file)

        return backups

    def backup_hosts(self, path_to_save: str = "") -> None:
        """
        Backup current system hosts file
        """
        try:
            if not path_to_save:
                backup_name = self.generate_backup_name()
                path_to_save = os.path.join(self.state.preferred_backup_path, backup_name)
            HostsFileHelper.write(path_to_save, self.state.file_content)
        except Exception:
            # TODO: handle error
            raise
