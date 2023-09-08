```python
import unittest
import sys

class TestDependencies(unittest.TestCase):
    def test_pyqt_dependency(self):
        try:
            from PyQt5 import QtWidgets
        except ImportError:
            self.fail("PyQt5 dependency not found.")

    def test_pyautogui_dependency(self):
        try:
            import pyautogui
        except ImportError:
            self.fail("pyautogui dependency not found.")

if __name__ == '__main__':
    unittest.main()
```