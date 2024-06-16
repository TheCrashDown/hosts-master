from src.backend.os_master import OSMaster


class HostsEditor:
    os_master: OSMaster

    file_content: list[str]

    def __init__(self):
        self.os_master = OSMaster()

        self.file_content = []

    @staticmethod
    def is_line_important(line: str):
        line = line.strip()
        return line and not line.startswith("#")

    def read_hosts(self):
        # os.access(self.os_master.hosts_path, os.R_OK)
        with open(self.os_master.hosts_path, "r") as hosts_file:
            lines = hosts_file.readlines()

        self.file_content = lines


        for line in self.file_content:
            if self.is_line_important(line):
                print(line.strip())

        print(self.file_content)

