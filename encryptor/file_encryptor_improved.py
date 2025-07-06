import argparse
import getpass
import os
import sys
import json
from encryptor import core

def parse_arguments():
    parser = argparse.ArgumentParser(description="File Encryption/Decryption Tool")
    parser.add_argument('--encrypt', action='store_true', help='Encrypt the input file.')
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the input file.')
    parser.add_argument('-i', '--input', type=str, help='Input file or folder path.')
    parser.add_argument('-o', '--output', type=str, help='Output file or folder path (optional).')
    parser.add_argument('-p', '--password', type=str, help='Password for encryption/decryption.')
    parser.add_argument('--json', action='store_true', help='Output result in JSON format.')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if not args.input:
        print("[-] Error: Input file or folder is required.")
        sys.exit(1)

    password = args.password or getpass.getpass("Enter password: ")

    # Auto-generate output file if not provided
    if args.output:
        output_path = args.output
    else:
        if args.encrypt:
            output_path = f"{args.input}.enc"
        elif args.decrypt:
            output_path = args.input.replace(".enc", ".dec.txt")
        else:
            output_path = f"{args.input}.out"

    # Encrypt or Decrypt
    try:
        if args.encrypt:
            if os.path.isdir(args.input):
                core.encrypt_folder(args.input, output_path, password)
                message = f"Encrypted folder {args.input} as {output_path}"
            else:
                core.encrypt_file(args.input, output_path, password)
                message = f"Encrypted {args.input} as {output_path}"
        elif args.decrypt:
            if os.path.isdir(args.input):
                core.decrypt_folder(args.input, output_path, password)
                message = f"Decrypted folder {args.input} to {output_path}"
            else:
                core.decrypt_file(args.input, output_path, password)
                message = f"Decrypted {args.input} to {output_path}"
        else:
            print("[-] Please specify --encrypt or --decrypt.")
            sys.exit(1)

        # Output
        if args.json:
            print(json.dumps({"status": "success", "message": message}))
        else:
            print(f"[+] {message}")

    except core.InvalidPasswordError:
        error_msg = "[-] Invalid password or corrupted file."
        if args.json:
            print(json.dumps({"status": "error", "message": error_msg}))
        else:
            print(error_msg)
        sys.exit(1)
    except Exception as e:
        error_msg = f"[-] Error: {str(e)}"
        if args.json:
            print(json.dumps({"status": "error", "message": error_msg}))
        else:
            print(error_msg)
        sys.exit(1)

if __name__ == '__main__':
    main()

