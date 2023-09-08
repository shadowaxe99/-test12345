```python
import time
from src.click_simulation import simulate_click

class Performance:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()

    def get_response_time(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        else:
            return None

    def check_performance(self):
        self.start_timer()
        simulate_click('left', 'single', (0, 0))
        self.stop_timer()
        response_time = self.get_response_time()

        if response_time is not None and response_time < 0.02:
            return True
        else:
            return False
```