import sys
import argparse
from keygen import key_gen
from encryptor import encrypt_file
from decryptor import decrypt_file


def create_parser():
    "Returns an instance of argpars.ArgumentParser"
    parser = argparse.ArgumentParser(description='''Takes in a filepath to a file for encryption and decryption''')
    parser.add_argument('-e', '--encrypt', help='The -e flag followed with a file path to a file initiates the'
                        ' encryptions process.')
    parser.add_argument('-d', '--decrypt', help='The -d flag followed with a file path to a file initiates the'
                        ' decrytpion process.')
    parser.add_argument('-k', '--keygen', help='the -k flag followed by keygen generates a file that contains a'
                        'secret key used for file encryption and decryption')
    return parser


def main(args):
    '''Encrypt This'''
    '''Takes command line argument to initiate different program functionality'''
    parser = create_parser()
    ns = parser.parse_args(args)

    encrypt = ns.encrypt
    decrypt = ns.decrypt
    keygen = ns.keygen

    if not ns:
        parser.print_usage()
        sys.exit(1)
    elif encrypt:
        encrypt_file(encrypt)
    elif decrypt:
        decrypt_file(decrypt)
    elif keygen:
        key_gen()


if __name__ == "__main__":
    main(sys.argv[1:])
