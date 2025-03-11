import sqlite3
import hashlib
import os
import base64
from cryptography.fernet import Fernet
import getpass
import secrets
import string

# Generate or load encryption key
def load_key():
    key_file = "key.key"
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as keyfile:
            keyfile.write(key)
    else:
        with open(key_file, "rb") as keyfile:
            key = keyfile.read()
    return Fernet(key)

encryption = load_key()

# Initialize database
def init_db():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            master_password_hash TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT,
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

# Hash master password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Setup master password
def setup_master_password():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    if not c.fetchone():
        master_password = getpass.getpass("Set a master password: ")
        confirm_password = getpass.getpass("Confirm master password: ")
        if master_password == confirm_password:
            c.execute("INSERT INTO users (master_password_hash) VALUES (?)", (hash_password(master_password),))
            conn.commit()
            print("Master password set successfully!")
        else:
            print("Passwords do not match. Try again.")
    conn.close()

# Verify master password
def verify_master_password():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT master_password_hash FROM users")
    stored_hash = c.fetchone()[0]
    conn.close()
    
    while True:
        entered_password = getpass.getpass("Enter your master password: ")
        if hash_password(entered_password) == stored_hash:
            print("Access granted!")
            break
        else:
            print("Incorrect password. Try again.")

# Encrypt password
def encrypt_password(password):
    return encryption.encrypt(password.encode()).decode()

# Decrypt password
def decrypt_password(encrypted_password):
    return encryption.decrypt(encrypted_password.encode()).decode()

# Generate strong password
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# Store a new password
def store_password():
    service = input("Enter service name: ")
    username = input("Enter username: ")
    password = input("Enter password (or leave blank to generate one): ")
    if not password:
        password = generate_password()
        print(f"Generated password: {password}")
    encrypted_password = encrypt_password(password)
    
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
              (service, username, encrypted_password))
    conn.commit()
    conn.close()
    print("Password stored successfully!")

# Retrieve stored passwords
def retrieve_passwords():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT service, username, password FROM passwords")
    data = c.fetchall()
    conn.close()
    
    print("\nStored Passwords:")
    for service, username, encrypted_password in data:
        decrypted_password = decrypt_password(encrypted_password)
        print(f"Service: {service}, Username: {username}, Password: {decrypted_password}")

# Main menu
def main():
    init_db()
    setup_master_password()
    verify_master_password()
    
    while True:
        print("\nPassword Manager")
        print("1. Store a new password")
        print("2. Retrieve stored passwords")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            store_password()
        elif choice == "2":
            retrieve_passwords()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
