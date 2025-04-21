from cryptography.fernet import Fernet

def decrypt_file(enc_file, output_file, key_file="vault.key"):
    with open(key_file, "rb") as f:
        key = f.read()

    with open(enc_file, "rb") as f:
        data = f.read()

    decrypted = Fernet(key).decrypt(data)
    with open(output_file, "wb") as f:
        f.write(decrypted)
    print(f"✅ Decrypted {enc_file} → {output_file}")