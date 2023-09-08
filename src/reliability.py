```python
import time
from datetime import datetime, timedelta

class Reliability:
    def __init__(self):
        self.start_time = datetime.now()
        self.downtime = timedelta()

    def record_downtime(self, downtime_start, downtime_end):
        self.downtime += downtime_end - downtime_start

    def get_uptime(self):
        total_time = datetime.now() - self.start_time
        uptime = total_time - self.downtime
        uptime_percentage = (uptime.total_seconds() / total_time.total_seconds()) * 100
        return round(uptime_percentage, 2)

reliability = Reliability()

# Example usage:
# downtime_start = datetime.now()
# time.sleep(5)  # downtime
# downtime_end = datetime.now()
# reliability.record_downtime(downtime_start, downtime_end)
# print(reliability.get_uptime())
```