from cryptography.fernet import Fernet

def encrypt_file(input_file, output_file, key_file="vault.key"):
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)

    with open(input_file, "rb") as f:
        data = f.read()

    encrypted = Fernet(key).encrypt(data)
    with open(output_file, "wb") as f:
        f.write(encrypted)
    print(f"✅ Encrypted {input_file} → {output_file}")