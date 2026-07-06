from cryptography.fernet import Fernet


def load_key():
    # loads key file generated in keygen.py
    with open("secret.key", "rb") as key_file:
        return key_file.read()


def encrypt_file(filename):
    # initiate fernet with key
    key = load_key()
    fernet = Fernet(key)

    # read the file contents
    with open(filename, 'rb') as file:
        file_data = file.read()

    # encryption time
    encrypted_data = fernet.encrypt(file_data)

    # overwrite file with encrypted data
    with open(filename, 'wb') as file:
        file.write(encrypted_data)
    print(f'{filename}: Encryption success!!')
