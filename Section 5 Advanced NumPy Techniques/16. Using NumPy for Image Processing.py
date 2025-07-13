import numpy as np
import imageio
import matplotlib.pyplot as plt

# Read the image from file
image = imageio.imread('color_image.jpg')

# Convert to grayscale using dot product with luminance weights
#gray_image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
negative_image =255 - image
plt.imshow(negative_image)
# Display the grayscale image
#plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.show()
