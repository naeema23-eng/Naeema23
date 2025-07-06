import unittest
import subprocess
import os

# Use the Python module path instead of installed CLI
CLI_COMMAND = ["python3", "-m", "encryptor.file_encryptor_improved"]

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.input_file = "tests/test_input.txt"
        self.password = "testpassword"
        self.encrypted_file = f"{self.input_file}.enc"
        self.decrypted_file = f"{self.input_file}.dec.txt"

        # Create a simple input file
        with open(self.input_file, "w") as f:
            f.write("This is a test message.")

    def tearDown(self):
        for file in [self.input_file, self.encrypted_file, self.decrypted_file]:
            if os.path.exists(file):
                os.remove(file)

    def run_cli(self, args):
        result = subprocess.run(CLI_COMMAND + args, capture_output=True, text=True)
        return result

    def test_encrypt_decrypt_flow(self):
        encrypt = self.run_cli(["--encrypt", "-i", self.input_file, "-p", self.password])
        self.assertIn("Encrypted", encrypt.stdout)

        decrypt = self.run_cli(["--decrypt", "-i", self.encrypted_file, "-p", self.password])
        self.assertIn("Decrypted", decrypt.stdout)

    def test_missing_arguments(self):
        result = self.run_cli([])
        self.assertIn("input file or folder is required", result.stdout.lower())

    def test_wrong_password(self):
        # Encrypt first
        self.run_cli(["--encrypt", "-i", self.input_file, "-p", self.password])

        # Try decrypting with wrong password
        decrypt = self.run_cli(["--decrypt", "-i", self.encrypted_file, "-p", "wrongpass"])
        self.assertIn("Invalid password", decrypt.stdout)

if __name__ == '__main__':
    unittest.main()
