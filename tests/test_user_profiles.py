```python
import unittest
from src import user_profiles

class TestUserProfiles(unittest.TestCase):

    def setUp(self):
        self.user_profiles = user_profiles.UserProfiles()

    def test_save_profile(self):
        profile_data = {
            'profile_name': 'Test',
            'click_type': 'left',
            'click_interval': 'seconds',
            'click_position': 'fixed',
            'click_limit': 'unlimited',
            'hotkeys': {'start/stop': 'F1', 'pause/resume': 'F2'}
        }
        self.user_profiles.save_profile(profile_data)
        self.assertIn('Test', self.user_profiles.profiles)

    def test_load_profile(self):
        profile_data = {
            'profile_name': 'Test',
            'click_type': 'left',
            'click_interval': 'seconds',
            'click_position': 'fixed',
            'click_limit': 'unlimited',
            'hotkeys': {'start/stop': 'F1', 'pause/resume': 'F2'}
        }
        self.user_profiles.save_profile(profile_data)
        loaded_profile = self.user_profiles.load_profile('Test')
        self.assertEqual(loaded_profile, profile_data)

    def test_delete_profile(self):
        profile_data = {
            'profile_name': 'Test',
            'click_type': 'left',
            'click_interval': 'seconds',
            'click_position': 'fixed',
            'click_limit': 'unlimited',
            'hotkeys': {'start/stop': 'F1', 'pause/resume': 'F2'}
        }
        self.user_profiles.save_profile(profile_data)
        self.user_profiles.delete_profile('Test')
        self.assertNotIn('Test', self.user_profiles.profiles)

if __name__ == '__main__':
    unittest.main()
```