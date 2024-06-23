import tkinter as tk
from tkinter import font, ttk

from src.backend import HostsManager, OSMaster


class GUI:
    root: tk.Tk
    hosts_manager: HostsManager

    def __init__(self, hosts_manager) -> None:
        self.hosts_manager = hosts_manager

        self._create_root()
        self._create_menu()
        self._create_interface()

    def _create_root(self) -> None:
        """
        Create root window
        """

        self.root = tk.Tk()
        self.root.title("Hosts Master")

        self.root.minsize(1200, 700)

    def _create_menu(self) -> None:
        menubar = tk.Menu()

        # =============== 1. File ===============
        tab_file = tk.Menu(menubar, tearoff=0)
        tab_file.add_command(label="Open system hosts", accelerator="Ctrl+O")
        tab_file.add_command(label="Open", accelerator="Ctrl+Shift+O")
        tab_file.add_command(label="Save", accelerator="Ctrl+S")
        tab_file.add_command(label="Save As...", accelerator="Ctrl+Shift+S")
        tab_file.add_separator()
        tab_file.add_command(label="Exit", accelerator="Ctrl+Q", command=self.exit)

        self.root.bind_all("<Control-q>", lambda _: self.exit())

        # =============== 2. Settings ===============
        tab_settings = tk.Menu(menubar, tearoff=0)
        tab_settings.add_command(label="Preferences")

        menubar.add_cascade(label="File", menu=tab_file)
        menubar.add_cascade(label="Settings", menu=tab_settings)
        self.root.config(menu=menubar)

    def _create_interface(self) -> None:
        self._create_navigation_frame()

        separator = ttk.Separator(self.root, orient="vertical")
        separator.pack(side=tk.LEFT, fill=tk.BOTH, padx=10)
        self._create_editor_frame()

    def _create_navigation_frame(self) -> None:
        frame = tk.Frame(self.root)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

        # subframe 1: hosts
        frame_hosts = tk.Frame(frame)
        frame_hosts.pack(side=tk.TOP, fill=tk.BOTH)

        hosts_label = tk.Label(frame_hosts, text="System hosts")
        hosts_label.pack(side=tk.TOP, fill=tk.BOTH)
        f = font.Font(hosts_label, hosts_label.cget("font"))
        f.configure(underline=True)
        hosts_label.configure(font=f)

        hosts_path = tk.Label(frame_hosts, text=OSMaster.hosts_path)
        hosts_path.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)

        # subframe 2: backups
        # frame_backups = tk.Frame(frame)
        # frame_backups.pack(side=tk.TOP, fill=tk.BOTH)

        # hosts_label = tk.Label(frame_backups, text="Backups")
        # hosts_label.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)
        # f = font.Font(hosts_label, hosts_label.cget("font"))
        # f.configure(underline=True)
        # hosts_label.configure(font=f)

        # hosts_path = tk.Label(frame_backups, text=OSMaster.hosts_path)
        # hosts_path.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)

    def _create_editor_frame(self) -> None:
        frame_editor = tk.Frame(self.root)
        frame_editor.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10)

        cancel_button = tk.Button(frame_editor, text="Cancel")
        cancel_button.pack(side=tk.RIGHT, anchor="se", padx=5, pady=5)

        backup_button = tk.Button(frame_editor, text="Save as backup")
        backup_button.pack(side=tk.RIGHT,anchor="se", padx=5, pady=5)

        save_button = tk.Button(frame_editor, text="Save to system")
        save_button.pack(side=tk.RIGHT, anchor="se", padx=5, pady=5)

    def start(self) -> None:
        self.root.mainloop()

    def exit(self) -> None:
        self.root.destroy()
