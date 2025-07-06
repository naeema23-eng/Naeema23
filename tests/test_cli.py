import unittest
import subprocess
import os

CLI_COMMAND = "file-encryptor"

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.input_file = "test_input.txt"
        self.encrypted_file = f"{self.input_file}.enc"
        with open(self.input_file, "w") as f:
            f.write("CLI test content.")
        self.password = "12345"

    def tearDown(self):
        for file in [self.input_file, self.encrypted_file, f"{self.input_file}.dec.txt"]:
            if os.path.exists(file):
                os.remove(file)

    def run_cli(self, args):
        return subprocess.run([CLI_COMMAND] + args, capture_output=True, text=True)

    def test_encrypt_decrypt_flow(self):
        encrypt = self.run_cli(["--encrypt", "-i", self.input_file, "-p", self.password])
        self.assertIn("Encrypted", encrypt.stdout)

        decrypt = self.run_cli(["--decrypt", "-i", self.encrypted_file, "-p", self.password])
        self.assertIn("Decrypted", decrypt.stdout)

    def test_missing_arguments(self):
        result = self.run_cli([])
        self.assertIn("Error", result.stdout)

    def test_wrong_password(self):
        self.run_cli(["--encrypt", "-i", self.input_file, "-p", self.password])
        decrypt = self.run_cli(["--decrypt", "-i", self.encrypted_file, "-p", "wrong"])
        self.assertIn("Invalid password", decrypt.stdout)

if __name__ == '__main__':
    unittest.main()
