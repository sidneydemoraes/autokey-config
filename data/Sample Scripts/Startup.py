# Enter script code

system.exec_command("authy %U")
system.exec_command("transmission-gtk %U")
system.exec_command("/usr/bin/firejail --name=vivaldi --dns=1.1.1.1 --dns=1.0.0.1 --net=wlp3s0 /usr/bin/vivaldi-stable %U")
keyboard.send_keys("<ctrl> + <alt> + t")
