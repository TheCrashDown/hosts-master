from src.backend import HostsManager as HostsManager
from src.gui import GUI


class HostsMaster:
    gui: GUI
    hosts_manager: HostsManager

    def __init__(self) -> None:
        self.hosts_manager = HostsManager()
        self.gui = GUI(hosts_manager=self.hosts_manager)

    def run(self) -> None:
        self.gui.start()
