from skimage import io, color
from skimage.metrics import structural_similarity as ssim

def compare_images(original_path, altered_path):
    # Load images
    original_image = io.imread(original_path)
    altered_image = io.imread(altered_path)

    # Convert images to grayscale
    original_gray = color.rgb2gray(original_image)
    altered_gray = color.rgb2gray(altered_image)

    # Compute structural similarity index
    similarity_index, _ = ssim(original_gray, altered_gray, full=True, data_range=altered_gray.max() - altered_gray.min())

    return similarity_index

if __name__ == "__main__":
    # Paths to the original and altered images
    original_image_path = "original_image.png"
    altered_image_path = "encoded_image.png"

    # Compare images
    similarity_index = compare_images(original_image_path, altered_image_path)

    # Print the similarity index
    print(f"Structural Similarity Index: {similarity_index}")

    # You can set a threshold to determine if the image is altered based on the similarity index
    threshold = 0.9  # Adjust this threshold as needed
    if similarity_index < threshold:
        print("The image may have been altered.")
    else:
        print("The image appears to be unchanged.")
