 # Password Manager

This project is a simple password manager built using Python. It securely stores and manages passwords, allowing users to add new passwords, view existing ones, and encrypt them for enhanced security.

## Python Fundamentals Employed

Here are some of the key Python language features used in this project:

- **Functions:** The code effectively utilizes functions to encapsulate specific tasks, making it more modular and reusable. This includes functions like `write_key()`, `load_key()`, `view()`, and `add()`.
- **File I/O:** The project demonstrates file handling capabilities to read and write data to files. It uses the `open()` function, `with` context manager, and `write()` and `read()` methods for file interactions.
- **Encryption:** The `cryptography` library is employed for password encryption and decryption, ensuring a higher level of security for stored passwords.
- **User Input:** The code takes user input through the `input()` function, enabling interactive password management and user choices.
- **Loops:** The `while` loop is used to create a continuous menu-driven interface, allowing users to repeatedly perform actions until they choose to quit.
- **Conditional Statements:** Conditional statements like `if` and `elif` are used to control the program's flow based on user input and handle different scenarios.

## Getting Started

1. **Install Dependencies:**
   ```bash
   pip install cryptography
   ```
2. **Run the Application:**
   ```bash
   python password_manager.py
   ```

## Additional Information

- **cryptography Library:** Explore the `cryptography` library for more advanced encryption features: [https://cryptography.io/en/latest/](https://cryptography.io/en/latest/)

## Contributing

Feel free to contribute to this project by suggesting improvements, fixing bugs, or adding new features.
