```python
import unittest
from src import hotkeys

class TestHotkeys(unittest.TestCase):

    def setUp(self):
        self.hotkeys = hotkeys.Hotkeys()

    def test_start_stop(self):
        self.hotkeys.set_start_stop('F1', 'F2')
        self.assertEqual(self.hotkeys.get_start_stop(), ('F1', 'F2'))

    def test_pause_resume(self):
        self.hotkeys.set_pause_resume('F3', 'F4')
        self.assertEqual(self.hotkeys.get_pause_resume(), ('F3', 'F4'))

if __name__ == '__main__':
    unittest.main()
```