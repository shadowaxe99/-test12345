```python
import unittest
from src import security

class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.security = security.Security()

    def test_encrypt(self):
        profile_data = {
            'click_type': 'left',
            'click_interval': '500ms',
            'click_position': 'fixed',
            'click_limit': 'unlimited',
            'hotkeys': {
                'start_stop': 'ctrl+shift+a',
                'pause_resume': 'ctrl+shift+s'
            }
        }
        encrypted_data = self.security.encrypt(profile_data)
        self.assertNotEqual(encrypted_data, profile_data)

    def test_decrypt(self):
        profile_data = {
            'click_type': 'left',
            'click_interval': '500ms',
            'click_position': 'fixed',
            'click_limit': 'unlimited',
            'hotkeys': {
                'start_stop': 'ctrl+shift+a',
                'pause_resume': 'ctrl+shift+s'
            }
        }
        encrypted_data = self.security.encrypt(profile_data)
        decrypted_data = self.security.decrypt(encrypted_data)
        self.assertEqual(decrypted_data, profile_data)

if __name__ == '__main__':
    unittest.main()
```