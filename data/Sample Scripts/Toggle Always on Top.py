# Enter script code
import subprocess

# Executa o comando wmctrl para alternar o estado "always on top" da janela ativa
subprocess.run(['wmctrl', '-r', ':ACTIVE:', '-b', 'toggle,above'])
