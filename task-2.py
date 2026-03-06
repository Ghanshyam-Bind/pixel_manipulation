from PIL import Image
import numpy as np
import random

def encrypt_image(image_path, key):

    img = Image.open(image_path)
    pixels = np.array(img)

    h, w, c = pixels.shape
    flat_pixels = pixels.reshape(-1, 3)

    random.seed(key)

    swaps = []

    for i in range(len(flat_pixels)):
        j = random.randint(0, len(flat_pixels)-1)

        flat_pixels[i], flat_pixels[j] = flat_pixels[j].copy(), flat_pixels[i].copy()

        swaps.append((i, j))

    encrypted_pixels = flat_pixels.reshape(h, w, c)

    Image.fromarray(encrypted_pixels.astype('uint8')).save("encrypted_image.png")

    print("Encrypted image saved as encrypted_image.png")

    return swaps


def decrypt_image(image_path, key):

    img = Image.open(image_path)
    pixels = np.array(img)

    h, w, c = pixels.shape
    flat_pixels = pixels.reshape(-1, 3)

    random.seed(key)

    swaps = []

    for i in range(len(flat_pixels)):
        j = random.randint(0, len(flat_pixels)-1)
        swaps.append((i, j))

    for i, j in reversed(swaps):
        flat_pixels[i], flat_pixels[j] = flat_pixels[j].copy(), flat_pixels[i].copy()

    decrypted_pixels = flat_pixels.reshape(h, w, c)

    Image.fromarray(decrypted_pixels.astype('uint8')).save("decrypted_image.png")

    print("Decrypted image saved as decrypted_image.png")


choice = input("Encrypt or Decrypt (e/d): ")
image_path = input("Enter image path: ")
key = int(input("Enter key: "))

if choice == "e":
    encrypt_image(image_path, key)

elif choice == "d":
    decrypt_image(image_path, key)

else:
    print("Invalid option")
