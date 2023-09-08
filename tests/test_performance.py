```python
import unittest
import time
from src import click_simulation

class TestPerformance(unittest.TestCase):

    def setUp(self):
        self.click_simulation = click_simulation.ClickSimulation()

    def test_response_time(self):
        start_time = time.time()
        self.click_simulation.simulate_click('left', 'single', (0, 0))
        end_time = time.time()
        response_time = end_time - start_time
        self.assertLess(response_time, 0.02, "Response time is more than 20ms")

if __name__ == '__main__':
    unittest.main()
```