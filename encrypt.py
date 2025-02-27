import cv2
import os

def encrypt_message(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not load image.")
        return

    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    d = {chr(i): i for i in range(256)}

    n, m, z = 0, 0, 0

    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite("Encryptedmsg.jpg", img)

    with open("password.txt", "w") as f:
        f.write(password)

    print("Encryption complete. Encrypted image saved as 'Encryptedmsg.jpg'.")
    os.system("start Encryptedmsg.jpg")
