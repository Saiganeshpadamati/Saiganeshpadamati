from cryptography.fernet import Fernet

# 🔑 Generate and save key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# 🔑 Load key from file
def load_key():
    return open("secret.key", "rb").read()

# 🔐 Encrypt file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

    print("✅ File encrypted successfully!")

# 🔓 Decrypt file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted = fernet.decrypt(encrypted_data)

    with open("decrypted_" + filename.replace(".enc", ""), "wb") as file:
        file.write(decrypted)

    print("✅ File decrypted successfully!")


if _name_ == "_main_":
    print("🔐 File Encryption Tool")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")

    choice = input("Enter choice: ")

    if choice == "1":
        generate_key()
        print("🔑 Key generated and saved as secret.key")
    elif choice == "2":
        filename = input("Enter filename to encrypt: ")
        encrypt_file(filename)
    elif choice == "3":
        filename = input("Enter filename to decrypt: ")
        decrypt_file(filename)
    else:
        print("❌ Invalid choice!")
