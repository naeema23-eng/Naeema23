from setuptools import setup, find_packages

setup(
    name='file-encryptor',
    version='1.0.0',
    description='Simple file encryption tool using Fernet',
    author='Naeema Alnaqbi',
    packages=find_packages(),
    install_requires=[
        'cryptography',
    ],
    entry_points={
        'console_scripts': [
            'file-encryptor=encryptor.file_encryptor_improved:main',
        ],
    },
)
