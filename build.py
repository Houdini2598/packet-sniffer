#!/usr/bin/env python3
# https://github.com/Houdini2598/packet-sniffer

__author__ = "Houdini"

import PyInstaller.__main__ as pyinstaller


"""Set up the arguments required by PyInstaller to build the Network
Packet Sniffer binary."""
pyinstaller.run(("packet_sniffer/core.py", "--onefile"))
