```python
import pyautogui

class ClickPosition:
    def __init__(self):
        self.position_type = None
        self.fixed_position = None

    def set_position_type(self, position_type):
        if position_type in ['fixed', 'variable']:
            self.position_type = position_type
        else:
            raise ValueError("Invalid position type. Choose 'fixed' or 'variable'.")

    def set_fixed_position(self, x, y):
        if self.position_type != 'fixed':
            raise ValueError("Position type is not set to 'fixed'.")
        self.fixed_position = (x, y)

    def get_click_position(self):
        if self.position_type == 'fixed':
            return self.fixed_position
        elif self.position_type == 'variable':
            return pyautogui.position()
        else:
            raise ValueError("Position type is not set.")
```