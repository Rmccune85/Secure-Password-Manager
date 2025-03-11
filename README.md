# Secure-Password-Manager
A Python-based encrypted password manager using AES encryption and SQLite. Stores passwords securely with a master password.
# Secure Password Manager 🔐

A simple, encrypted password manager built with Python. This project securely stores and retrieves passwords using AES encryption and an SQLite database, ensuring your sensitive data remains safe.

---

## 📌 Features
- **AES encryption** for password security 🔒
- **Master password authentication** to restrict access 🔑
- **Secure password storage** using SQLite 📂
- **Strong password generator** for creating secure passwords 🔢
- **Command-line interface (CLI)** for easy usage 🖥️

---

## 🚀 Installation
### **1️⃣ Install Python (3.8+ Required)**
- Download and install Python from [python.org](https://www.python.org/downloads/).

### **2️⃣ Install Required Libraries**
Open your terminal or command prompt and run:
```bash
pip install cryptography sqlite3 hashlib getpass
```

### **3️⃣ Download the Project**
- Clone the GitHub repository:
  ```bash
  git clone https://github.com/YourGitHubUsername/Secure-Password-Manager.git
  cd Secure-Password-Manager
  ```
  **OR** manually download and extract the files.

### **4️⃣ Run the Script**
Start the password manager by running:
```bash
python password_manager.py
```

---

## 📖 How to Use
### **🔹 First-Time Setup**
1. When you first run the program, you will be prompted to **set a master password**.
2. This password will be required to access stored credentials in the future.

### **🔹 Storing a Password**
1. Choose `1. Store a new password`.
2. Enter the **service name** (e.g., GitHub, Netflix).
3. Enter the **username** for that service.
4. Enter a password **or leave it blank** to generate a secure one.
5. Passwords are encrypted and securely stored.

### **🔹 Retrieving Passwords**
1. Choose `2. Retrieve stored passwords`.
2. The program will display stored credentials **(decrypted securely)**.

### **🔹 Exiting**
- Select `3. Exit` to close the program.

---

## 🛡 Security Considerations
✔ Your **master password is hashed** and never stored in plaintext.  
✔ All stored passwords are **AES-encrypted** for maximum security.  
✔ The SQLite database ensures **local-only** access, avoiding cloud vulnerabilities.  

---

## 🎯 Future Enhancements (Planned)
🔸 **Graphical User Interface (GUI) version** with Tkinter.  
🔸 **Password strength checker** before saving credentials.  
🔸 **Search function** to retrieve specific passwords quickly.  
🔸 **Auto-backup feature** for secure database storage.  

---

## 📜 License
This project is open-source under the **MIT License**. Feel free to use and modify it!

---

## 🙌 Contributing
Want to improve this project? Contributions are welcome! Fork the repo and submit a pull request.

---

## 📬 Contact
For any questions or feedback, reach out via:
📧 Email: [YourEmail@example.com](mailto:YourEmail@example.com)  
🐙 GitHub: [YourGitHubProfile](https://github.com/YourGitHubUsername)  

---

### **🔗 [View on GitHub](https://github.com/YourGitHubUsername/Secure-Password-Manager)**

