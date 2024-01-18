# Image Steganography and Alteration Detection

This project focuses on image steganography, utilizing the Python Imaging Library (PIL) to hide text within images using the Least Significant Bit (LSB) encoding technique. Additionally, it provides a mechanism for detecting alterations made to images through a structural similarity index comparison.

## Steganography

The steganography functionality includes two main functions:

### 1. text_to_binary

This function converts text into its 8-bit binary representation.

### 2. hide_text_in_image

This function hides text within an image using the LSB encoding technique. It reads text from a specified file, converts it to binary, and embeds it into the image pixels.

## Alteration Detection

The alteration detection feature is provided by the `compare_images` function, which computes the structural similarity index between the original and altered images. This index is then used to determine whether the image has been altered.

## Dependencies

- Python Imaging Library (PIL)
- scikit-image

You can install the dependencies using the following:

```bash
pip install Pillow scikit-image
```
