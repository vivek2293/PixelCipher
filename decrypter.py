from PIL import Image

# Function to convert binary to text
def binary_to_text(binary_data):
    # Convert binary data to text by grouping 8 bits at a time and converting to ASCII
    text = ''.join([chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)])
    return text

# Function to extract text from an image using LSB (Least Significant Bit) encoding
def extract_text_from_image(image_path, output_file_path, delimiter="1111111111111110"):
    # Open the encoded image
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB mode

    # Get the pixel values of the image
    pixels = list(img.getdata())

    # Extract the binary text from the LSB of each color channel
    binary_text = ''.join([str(pixel[i] & 1) for pixel in pixels for i in range(3)])

    # Find the index of the delimiter in the binary text
    delimiter_index = binary_text.find(delimiter)

    # Extract binary text before the delimiter
    binary_text = binary_text[:delimiter_index]

    # Convert binary text to readable text
    extracted_text = binary_to_text(binary_text)

    # Write the extracted text to an external file
    with open(output_file_path, 'w') as file:
        file.write(extracted_text)

# Main function
if __name__ == "__main__":
    # Input file paths
    encoded_image_path = "encoded_image.png"
    output_file_path = "extracted_text.txt"

    # Call the function to extract text from the encoded image
    extract_text_from_image(encoded_image_path, output_file_path)

    # Print a message indicating the success of the extraction
    print("Extracted Text has been written to:", output_file_path)
