import encrypt
import decrypt
import cv2

def main():
    image_path = input("Enter the path of the image file: ")

    img = cv2.imread(image_path)
    if img is None:
        print("Invalid image path. Please check the file location.")
        return

    cv2.imwrite("mypic.jpg", img)

    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").strip().lower()

    if choice == 'e':
        encrypt.encrypt_message(image_path)  
    elif choice == 'd':
        decrypt.decrypt_message(image_path)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
