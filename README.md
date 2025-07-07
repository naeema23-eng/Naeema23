# 🔐 File Encryptor CLI (Python)

A simple and secure command-line tool to encrypt and decrypt files or folders using AES encryption, written in Python.
Includes optional Docker support and CI testing with GitHub Actions.

---

## 🕹️ Features

- Encrypt and decrypt files and folders securely
- Password-based encryption (PBKDF2 + AES)
- Automatic output file naming
- Simple command-line interface with clear logs
- Unit and CLI tests with GitHub Actions CI
- Docker support for isolated runs

---

## 🛠️ Build & Run Locally

### 🔧 Clone the repository:

```bash
git clone https://github.com/naeema23-eng/Naeema23.git
cd Naeema23
```

### 🔧 Install as a package:

```bash
pip install .
```

---

## 🔧 Usage

### 🔐 Encrypt a file:

```bash
file-encryptor --encrypt -i data/secret.txt -p yourpassword
```

### 🔒 Decrypt a file:

```bash
file-encryptor --decrypt -i data/secret.txt.enc -p yourpassword
```

The encrypted/decrypted files will be saved in the same folder by default.

---

## 🐳 Run with Docker (Optional)

### 🔧 Build the Docker image:

```bash
docker build -t file-encryptor .
```

### 🔐 Run encryption:

```bash
docker run --rm -v "$PWD":/data file-encryptor --encrypt -i /data/secret.txt -p yourpassword
```

### 🔒 Run decryption:

```bash
docker run --rm -v "$PWD":/data file-encryptor --decrypt -i /data/secret.txt.enc -p yourpassword
```

---

## 🔧 Run Tests

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

---

## 🔢 CI Pipeline

GitHub Actions workflow runs automatically on each push to run the tests.

