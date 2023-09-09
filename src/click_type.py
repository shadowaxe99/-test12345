```python
import pyautogui

class ClickType:
    def __init__(self):
        self.click_type = "left"

    def set_click_type(self, click_type):
        if click_type in ["left", "right", "middle"]:
            self.click_type = click_type
        else:
            raise ValueError("Invalid click type. Choose from 'left', 'right', or 'middle'.")

    def simulate_click(self):
        if self.click_type == "left":
            pyautogui.click(button='left')
        elif self.click_type == "right":
            pyautogui.click(button='right')
        elif self.click_type == "middle":
            pyautogui.click(button='middle')
        else:
            raise ValueError("Invalid click type. Choose from 'left', 'right', or 'middle'.")
```