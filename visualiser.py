import matplotlib.pyplot as plt
import numpy as np
from skimage import io

# Filenames of the original and altered images
original_image_filename = "original_image.png"
altered_image_filename = "encoded_image.png"

# Load original and altered images
original_image = io.imread(original_image_filename)
altered_image = io.imread(altered_image_filename)

# Compute absolute difference
diff_image = np.abs(original_image - altered_image)

# Plot original, altered, and difference images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(original_image)
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(altered_image)
plt.title('Altered Image')

plt.subplot(1, 3, 3)
plt.imshow(diff_image, cmap='gray')
plt.title('Difference Image')

plt.show()
