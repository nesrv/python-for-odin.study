from sys import *
import subprocess


if platform == "win32":
    subprocess.call("mspaint")
elif platform.startswith("linux"):
    subprocess.call("gnome-calculator")
    subprocess.Popen(["ls -l"])
