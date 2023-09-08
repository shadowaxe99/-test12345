```python
import json
import os
from cryptography.fernet import Fernet

class UserProfile:
    def __init__(self):
        self.profiles = {}
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def save_profile(self, profile_name, click_type, click_interval, click_position, click_limit, hotkeys):
        profile_data = {
            'click_type': click_type,
            'click_interval': click_interval,
            'click_position': click_position,
            'click_limit': click_limit,
            'hotkeys': hotkeys
        }
        encrypted_data = self.cipher_suite.encrypt(json.dumps(profile_data).encode())
        self.profiles[profile_name] = encrypted_data

    def load_profile(self, profile_name):
        if profile_name in self.profiles:
            encrypted_data = self.profiles[profile_name]
            decrypted_data = self.cipher_suite.decrypt(encrypted_data)
            return json.loads(decrypted_data.decode())
        else:
            return None

    def delete_profile(self, profile_name):
        if profile_name in self.profiles:
            del self.profiles[profile_name]

    def save_profiles_to_disk(self):
        with open('user_profiles.json', 'w') as f:
            json.dump(self.profiles, f)

    def load_profiles_from_disk(self):
        if os.path.exists('user_profiles.json'):
            with open('user_profiles.json', 'r') as f:
                self.profiles = json.load(f)
```
