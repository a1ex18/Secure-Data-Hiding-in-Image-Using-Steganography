import cv2
import numpy as np

def decrypt_message(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not load encrypted image.")
        return

    try:
        with open("password.txt", "r") as f:
            saved_password = f.read().strip()
    except FileNotFoundError:
        print("Error: Password file not found.")
        return

    pas = input("Enter passcode for decryption: ")

    if pas == saved_password:
        c = {i: chr(i) for i in range(256)}  # Ensure mapping for all possible values

        message = ""
        n, m, z = 0, 0, 0
        rows, cols, _ = img.shape  # Get image dimensions

        while n < rows and m < cols:  # Ensure we don't go out of bounds
            pixel_value = int(img[n, m, z])  # Convert np.uint8 to int
            if pixel_value == 0:
                break
            message += c.get(pixel_value, '?')  # Safely get character
            n += 1
            m += 1
            z = (z + 1) % 3  # Cycle through color channels

        print("Decrypted message:", message)
    else:
        print("Invalid password!")
