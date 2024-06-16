import platform

if platform.system().lower() == "windows":
    from src.backend.os_master._windows import WindowsMaster as OSMaster
elif platform.system().lower() == "darwin":
    from src.backend.os_master._darwin import DarwinMaster as OSMaster
elif platform.system().lower() == "linux":
    from src.backend.os_master._linux import LinuxMaster as OSMaster
else:
    raise OSError("Unsupported platform '{}'".format(platform.system()))

__all__ = ["OSMaster"]
