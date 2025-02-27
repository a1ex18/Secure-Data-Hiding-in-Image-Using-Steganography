**Image Steganography using OpenCV
Overview**
This project implements image steganography using Python and OpenCV, allowing users to hide a secret message inside an image and later retrieve it using a password-protected decryption process.

**Features**

✅ Hide a secret message inside an image using pixel encoding
✅ Password-protected encryption and decryption
✅ Uses OpenCV for image processing
✅ Simple command-line interface

**Technologies Used**

Python
OpenCV
NumPy

**Installation**

1. Clone the Repository
git clone https://github.com/yourusername/steganography-project.git
cd steganography-project
**2. Install Dependencies**

Make sure you have Python installed, then install required libraries:
pip install opencv-python numpy

**Usage**

**1. Run the Main Script**
python stego.py

You will be prompted to enter the image path.
Choose (E) Encrypt or (D) Decrypt.

**2. Encryption Process**

Enter a secret message and password.
The encrypted image is saved as Encryptedmsg.jpg.

**3. Decryption Process**

Enter the correct password to retrieve the hidden message.

Project Files

📂 stego.py - Main script to run the project

📂 encrypt.py - Encrypts a message into an image

📂 decrypt.py - Extracts the hidden message from an image

📂 password.txt - Stores the encryption password (for testing)

**License**

This project is open-source and available under the MIT License.

Contributors

👤 a1ex18
