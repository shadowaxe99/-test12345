```python
import unittest
from src import reliability

class TestReliability(unittest.TestCase):

    def setUp(self):
        self.reliability = reliability.Reliability()

    def test_uptime(self):
        uptime = self.reliability.get_uptime()
        self.assertGreaterEqual(uptime, 99.9, "Uptime is less than 99.9%")

    def test_no_crashes(self):
        crashes = self.reliability.get_crashes()
        self.assertEqual(crashes, 0, "There were crashes")

if __name__ == '__main__':
    unittest.main()
```