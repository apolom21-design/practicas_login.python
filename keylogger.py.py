from pynput.keyboard import Listener
 
def keystore(key):
     print("Tecla presionada: {0}".format(key))
     
with Listener(on_press=keystore) as input_keyboard:
    
    input_keyboard.join()
     