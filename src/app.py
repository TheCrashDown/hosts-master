from src.backend import HostsManager as HostsManager
from src.gui import GUI


class HostsMaster:
    gui: GUI
    hosts_manager: HostsManager

    def __init__(self) -> None:
        self.gui = GUI()
        self.hosts_manager = HostsManager()
