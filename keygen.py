from cryptography.fernet import Fernet


def key_gen():
    """Generates secure and unique cryptographic key
    and save it to a file locally to be used for
    decryption."""

    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Your 'secret.key' has successfully been generated and saved.")

    if __name__ == "__main__":
        key_gen()
