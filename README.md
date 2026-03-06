#Pixel Manipulation for Image Encryption.

A simple Python project that demonstrates **basic image encryption using pixel manipulation**.
The program encrypts an image by randomly swapping pixel positions based on a **key**, and decrypts it by reversing the swaps using the same key.

This project helps understand **image processing and basic encryption concepts**.

🚀 Features

* Encrypt images using **pixel swapping technique**
* Decrypt encrypted images using the **same key**
* Works with **PNG / JPG images**
* Demonstrates **pixel-level manipulation**
* Uses **key-based reversible encryption**

🧠 How It Works

1. The image is converted into a **pixel array**.
2. Pixels are **flattened into a list**.
3. Using a **key-based random generator**, pixel positions are swapped.
4. The scrambled pixels create the **encrypted image**.
5. Decryption reverses the same swaps using the same key.

Because the random swaps are generated using the same key, the original image can be restored.

📦 Installation

Install required libraries:
pip install pillow numpy

## ▶️ How to Run

Run the script:

task-2.py

Program will ask:

Encrypt or Decrypt (e/d):

Enter image path:

Enter key:

💻 Example

Encrypt image:-

Encrypt or Decrypt (e/d): e

Enter image path: Original.jpg

Enter key: 10

Encrypted image saved as encrypted_image.png

Output:

encrypted_image.png

Decrypt image:-

Encrypt or Decrypt (e/d): d

Enter image path: encrypted_image.png

Enter key: 10

Decrypted image saved as decrypted_image.png

Output:

decrypted_image.png

🎯 Learning Outcomes
This project demonstrates:

* Pixel-level image representation
* RGB value manipulation
* Key-based reversible encryption
* Practical use of **NumPy arrays in image processing**

⚠️ Note
This encryption technique is **for educational purposes only** and is not secure for real-world cryptographic applications.

👨‍💻 Author
Ghanshyam Bind
