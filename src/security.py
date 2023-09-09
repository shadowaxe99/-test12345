```python
from cryptography.fernet import Fernet

class Security:

    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_profile(self, profile_data):
        encoded_text = profile_data.encode()
        cipher_text = self.cipher_suite.encrypt(encoded_text)
        return cipher_text

    def decrypt_profile(self, cipher_text):
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text.decode()

security = Security()
```