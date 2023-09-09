```python
import unittest
from src.click_interval import set_click_interval

class TestClickInterval(unittest.TestCase):

    def setUp(self):
        self.click_interval = set_click_interval

    def test_set_click_interval_milliseconds(self):
        self.assertEqual(self.click_interval(500, 'milliseconds'), 0.5)

    def test_set_click_interval_seconds(self):
        self.assertEqual(self.click_interval(2, 'seconds'), 2)

    def test_set_click_interval_minutes(self):
        self.assertEqual(self.click_interval(1, 'minutes'), 60)

    def test_set_click_interval_invalid_unit(self):
        with self.assertRaises(ValueError):
            self.click_interval(1, 'hours')

    def test_set_click_interval_negative_time(self):
        with self.assertRaises(ValueError):
            self.click_interval(-1, 'seconds')

if __name__ == '__main__':
    unittest.main()
```