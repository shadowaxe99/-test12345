```python
import pyautogui
from pynput import keyboard

class Hotkeys:
    def __init__(self):
        self.hotkeys = {
            'start_stop': '<f1>',
            'pause_resume': '<f2>'
        }

    def start_stop(self):
        # Function to start or stop the auto-clicker
        pass

    def pause_resume(self):
        # Function to pause or resume the auto-clicker
        pass

    def set_hotkeys(self, start_stop, pause_resume):
        self.hotkeys['start_stop'] = start_stop
        self.hotkeys['pause_resume'] = pause_resume

    def get_hotkeys(self):
        return self.hotkeys

    def listen(self):
        with keyboard.GlobalHotKeys({
            self.hotkeys['start_stop']: self.start_stop,
            self.hotkeys['pause_resume']: self.pause_resume
        }) as h:
            h.join()
```