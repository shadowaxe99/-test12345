```python
import unittest
import platform
import psutil

class TestSystemRequirements(unittest.TestCase):

    def test_os(self):
        current_os = platform.system()
        self.assertIn(current_os, ["Windows", "Darwin", "Linux"])

    def test_os_version(self):
        if platform.system() == "Windows":
            self.assertTrue(platform.release() in ["10", "11"])
        elif platform.system() == "Darwin":
            self.assertTrue(float(platform.mac_ver()[0][:4]) >= 10.15)
        elif platform.system() == "Linux":
            pass  # No specific version requirement for Linux

    def test_ram(self):
        ram = psutil.virtual_memory().total / (1024.0 ** 3)
        self.assertGreaterEqual(ram, 0.5)

    def test_disk_space(self):
        disk_space = psutil.disk_usage('/').free / (1024.0 ** 3)
        self.assertGreaterEqual(disk_space, 50)

if __name__ == '__main__':
    unittest.main()
```