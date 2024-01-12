from PIL import Image

# Function to convert text to binary
def text_to_binary(text):
    # Convert each character in the text to its 8-bit binary representation
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data

# Function to hide text in an image
def hide_text_in_image(image_path, output_path, text_file_path, delimiter="1111111111111110"):
    # Open the original image
    img = Image.open(image_path)

    # Ensure the image is in RGB mode
    img = img.convert('RGB')

    # Read text from the file
    with open(text_file_path, 'r') as file:
        text_to_hide = file.read()

    # Convert the text to binary
    binary_text = text_to_binary(text_to_hide)

    # Add the delimiter to the binary text
    binary_text_with_delimiter = binary_text + delimiter

    # Get the pixels of the original image
    pixels = list(img.getdata())

    # Create a list to store the modified pixels
    new_pixels = []

    # Initialize the index for the binary text
    text_index = 0

    # Iterate through each pixel in the image
    for pixel in pixels:
        # Create a new pixel with the same RGB values as the original pixel
        new_pixel = list(pixel)

        # Iterate through each color channel (RGB)
        for i in range(3):
            # Check if there are more bits to encode
            if text_index < len(binary_text_with_delimiter):
                # Modify the least significant bit of the color channel with a bit from the binary text
                new_pixel[i] = (pixel[i] & 0b11111110) | int(binary_text_with_delimiter[text_index], 2)
                text_index += 1
            else:
                break  # Break the inner loop if text is fully encoded

        # Append the modified pixel to the list
        new_pixels.append(tuple(new_pixel))

    # Create a new image with the modified pixels
    new_img = Image.new('RGB', img.size)
    new_img.putdata(new_pixels)

    # Save the new image
    new_img.save(output_path)

# Main function
if __name__ == "__main__":
    # Input file paths
    image_path = "original_image.png"
    output_path = "encoded_image.png"
    text_file_path = "text_to_hide.txt"

    # Call the function to hide text in the image
    hide_text_in_image(image_path, output_path, text_file_path)
