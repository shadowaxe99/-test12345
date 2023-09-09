```python
import platform
import psutil

class SystemRequirements:
    def __init__(self):
        self.required_os = ['Windows 10', 'Windows 11', 'macOS 10.15', 'Linux']
        self.required_ram = 512  # in MB
        self.required_disk_space = 50  # in MB

    def check_system(self):
        return self.check_os() and self.check_ram() and self.check_disk_space()

    def check_os(self):
        current_os = platform.system()
        if 'Windows' in current_os:
            version = platform.win32_ver()[0]
            current_os = current_os + ' ' + version
        elif 'Darwin' in current_os:
            current_os = 'macOS ' + platform.mac_ver()[0][:4]
        return current_os in self.required_os

    def check_ram(self):
        ram = psutil.virtual_memory()
        total_ram = ram.total / (1024 ** 2)  # Convert to MB
        return total_ram >= self.required_ram

    def check_disk_space(self):
        disk = psutil.disk_usage('/')
        free_disk_space = disk.free / (1024 ** 2)  # Convert to MB
        return free_disk_space >= self.required_disk_space


if __name__ == "__main__":
    system_req = SystemRequirements()
    if system_req.check_system():
        print("System requirements met.")
    else:
        print("System requirements not met.")
```