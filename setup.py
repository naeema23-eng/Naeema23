from setuptools import setup, find_packages

setup(
    name='file-encryptor',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'cryptography'
    ],
    entry_points={
        'console_scripts': [
            'file-encryptor = encryptor.file_encryptor_improved:main',
        ],
    },
    author='Your Name',
    description='A simple file encryption/decryption CLI tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
