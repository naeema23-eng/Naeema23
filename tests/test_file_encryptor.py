import unittest
import os
from encryptor import core

class TestFileEncryptor(unittest.TestCase):

    def setUp(self):
        self.password = "securepassword"
        self.input_file = "test_secret.txt"
        self.encrypted_file = "test_secret.enc"
        self.decrypted_file = "test_secret.dec.txt"
        with open(self.input_file, "w") as f:
            f.write("This is a secret message.")

    def tearDown(self):
        for file in [self.input_file, self.encrypted_file, self.decrypted_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_encryption_and_decryption(self):
        core.encrypt_file(self.input_file, self.encrypted_file, self.password)
        core.decrypt_file(self.encrypted_file, self.decrypted_file, self.password)

        with open(self.decrypted_file, "r") as f:
            decrypted_content = f.read()

        self.assertEqual(decrypted_content, "This is a secret message.")

    def test_invalid_password(self):
        core.encrypt_file(self.input_file, self.encrypted_file, self.password)
        with self.assertRaises(core.InvalidPasswordError):
            core.decrypt_file(self.encrypted_file, self.decrypted_file, "wrongpassword")

if __name__ == '__main__':
    unittest.main()
