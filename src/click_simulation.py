```python
import pyautogui

class ClickSimulation:
    def __init__(self):
        self.click_type = 'left'
        self.click_count = 1

    def set_click_type(self, click_type):
        self.click_type = click_type

    def set_click_count(self, click_count):
        self.click_count = click_count

    def simulate_click(self):
        if self.click_count == 1:
            pyautogui.click(button=self.click_type)
        elif self.click_count == 2:
            pyautogui.doubleClick(button=self.click_type)
```