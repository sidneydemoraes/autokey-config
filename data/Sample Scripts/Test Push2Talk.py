# Enter script code
#try:
#    import keyboard as mykb
#except ModuleNotFoundError:
    #pyenv_shims = "/home/sid/.pyenv/shims"
    #python_executable = f"{pyenv_shims}/python"
#    import subprocess
#    import sys
#    subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])
#    import keyboard as mykb

#dialog.info_dialog("Teste", "AAA")

#expected_action = 'alt+a'

#keyboard.send(expected_action)

#while mykb.is_pressed('ctrl+space'):
#    time.sleep(0.5)
    
#keyboard.send(expected_action)

for i in range(5):
    print("Loop iteration", i+1)
    time.sleep(1)
    mods = keyboard.mediator._get_modifiers_on()
    print(mods)


#dialog.info_dialog("Teste", "BBB")

#print('Ending operation')