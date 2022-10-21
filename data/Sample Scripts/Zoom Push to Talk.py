# Enter script code
import os

import evdev
    
    
lockfile = '.p2t.lockfile'
device_path = '/dev/input/event6'
hotkey = 'KEY_F1'
hold_action = 2
expected_action = '<alt>+A'

try:
  open(lockfile)
except FileNotFoundError:
  with open(lockfile, 'w'):
    
    device = evdev.InputDevice(device_path)
    keyboard.send_keys(expected_action)
    
    for event in device.read_loop():
      if event.type == evdev.ecodes.EV_KEY:
        category = evdev.categorize(event)
        
        if category.keycode != hotkey or category.keystate != hold_action:
          break
          
        print(category.keycode, type(category.keycode), category.keystate)
    
  keyboard.send_keys(expected_action)
  os.remove(lockfile)
  #print('Ending operation')