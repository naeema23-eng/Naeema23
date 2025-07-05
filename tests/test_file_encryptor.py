import unittest
import sys
import os

# Ensure the parent directory is in the path so we can import the encryptor module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from encryptor.file_encryptor_improved import encrypt_file, decrypt_file


class TestFileEncryptor(unittest.TestCase):

    def setUp(self):
        self.test_input = "test_secret.txt"
        self.encrypted_output = "test_secret.enc"
        self.decrypted_output = "test_secret.dec.txt"
        self.password = "TestPass123!"

        # Create a dummy file to encrypt
        with open(self.test_input, "w") as f:
            f.write("This is a secret message.")

    def tearDown(self):
        # Clean up test files
        for file in [self.test_input, self.encrypted_output, self.decrypted_output]:
            if os.path.exists(file):
                os.remove(file)

    def test_encryption_and_decryption(self):
        # Encrypt the file
        encrypt_file(self.test_input, self.encrypted_output, self.password)
        self.assertTrue(os.path.exists(self.encrypted_output), "Encrypted file was not created.")

        # Decrypt the file
        decrypt_file(self.encrypted_output, self.decrypted_output, self.password)
        self.assertTrue(os.path.exists(self.decrypted_output), "Decrypted file was not created.")

        # Verify that the decrypted content matches the original
        with open(self.test_input, "r") as original, open(self.decrypted_output, "r") as decrypted:
            self.assertEqual(original.read(), decrypted.read(), "Decrypted content does not match original.")


if __name__ == '__main__':
    unittest.main()


