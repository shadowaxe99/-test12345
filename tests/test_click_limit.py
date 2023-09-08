```python
import unittest
from src.click_limit import ClickLimit

class TestClickLimit(unittest.TestCase):

    def setUp(self):
        self.click_limit = ClickLimit()

    def test_unlimited_clicks(self):
        self.click_limit.set_click_limit('unlimited')
        self.assertEqual(self.click_limit.get_click_limit(), 'unlimited')

    def test_limited_clicks(self):
        self.click_limit.set_click_limit(100)
        self.assertEqual(self.click_limit.get_click_limit(), 100)

    def test_invalid_click_limit(self):
        with self.assertRaises(ValueError):
            self.click_limit.set_click_limit(-1)

if __name__ == '__main__':
    unittest.main()
```