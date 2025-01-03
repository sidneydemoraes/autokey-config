# Enter script code
import subprocess

commands = [
    "gnome-terminal",
    "gtk-launch transmission-gtk",
    "gtk-launch vivaldi-stable"
]

processes = [subprocess.Popen(command, shell=True) for command in commands]