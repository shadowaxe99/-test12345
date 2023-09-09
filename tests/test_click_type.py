```python
import unittest
from src.click_type import set_click_type

class TestClickType(unittest.TestCase):

    def setUp(self):
        self.click_types = ['left', 'right', 'middle']

    def test_set_click_type(self):
        for click_type in self.click_types:
            result = set_click_type(click_type)
            self.assertEqual(result, click_type)

if __name__ == '__main__':
    unittest.main()
```