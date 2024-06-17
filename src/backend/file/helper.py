import os


class HostsFileHelper:
    """Helper tool to work with hosts files"""

    @staticmethod
    def is_line_important(line: str) -> bool:
        """
        Check if line from hosts file is relevant (it is not blanc and not commented)

        Args:
            line: str - line to check

        Returns:
            bool
        """

        line = line.strip()
        return line and not line.startswith("#")

    @staticmethod
    def read_hosts(path: str) -> list[str]:
        """
        Read hosts-format file from provided path

        Args:
            path: str - path to read

        Returns:
            list[str] - file content
        """

        if not os.path.exists(path):
            raise FileNotFoundError(
                f"Can't read hosts file from path '{path}'. " "File does not exist."
            )

        if not os.access(path, os.R_OK):
            raise PermissionError(
                f"Can't read hosts file from path '{path}'. "
                "File does not exist or you don't have permission to read it."
            )

        with open(path, "r") as hosts_file:
            lines = hosts_file.readlines()

        return lines

    @staticmethod
    def write_hosts(path: str, lines: list[str]) -> None:
        """
        Write hosts-format file to provided path

        Args:
            path: str - path to write
            lines: list[str] - file content

        Returns:
            None
        """

        if not os.access(path, os.W_OK):
            raise PermissionError(
                f"Can't write hosts file to path '{path}'. "
                "You don't have permission to create or edit it."
            )

        with open(path, "w") as hosts_file:
            hosts_file.writelines(lines)
