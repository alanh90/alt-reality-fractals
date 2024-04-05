import numpy as np
import matplotlib.pyplot as plt


def generate_image(binary_string):
    # Convert the binary string to a 2D array
    image_data = np.array([int(x) for x in binary_string], dtype=np.uint8)
    image_data = image_data.reshape((16, 16))

    return image_data


# Set the image dimensions
width, height = 16, 16

# Generate all possible binary strings of length 256 (16x16)
binary_strings = [format(i, '0256b') for i in range(2 ** 256)]

# Create a grid of subplots to display the images
num_images = len(binary_strings)
num_cols = 10
num_rows = num_images // num_cols + 1

fig, axes = plt.subplots(num_rows, num_cols, figsize=(20, 20))

# Generate and display each image
for i, binary_string in enumerate(binary_strings):
    image = generate_image(binary_string)
    row = i // num_cols
    col = i % num_cols
    axes[row, col].imshow(image, cmap='binary')
    axes[row, col].axis('off')

# Remove any unused subplots
for i in range(num_images, num_rows * num_cols):
    row = i // num_cols
    col = i % num_cols
    fig.delaxes(axes[row, col])

plt.tight_layout()
plt.show()