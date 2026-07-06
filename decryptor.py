from cryptography.fernet import Fernet


def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()


def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    # reads encrypted file contents
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    # decrypts the data
    decrypted_data = fernet.decrypt(encrypted_data)

    # overwrites the file the original decrypted data
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print(f'{filename}: Success decryption complete!')
