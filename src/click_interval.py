```python
import time

class ClickInterval:
    def __init__(self):
        self.click_interval = 0

    def set_click_interval(self, interval, unit):
        if unit == 'milliseconds':
            self.click_interval = interval / 1000
        elif unit == 'seconds':
            self.click_interval = interval
        elif unit == 'minutes':
            self.click_interval = interval * 60
        else:
            raise ValueError("Invalid unit. Please choose from 'milliseconds', 'seconds', or 'minutes'.")

    def get_click_interval(self):
        return self.click_interval

    def wait_for_interval(self):
        time.sleep(self.click_interval)
```