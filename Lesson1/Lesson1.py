import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = [15, 10]

# Load an image (you can freely chose any image you like)
img = cv2.imread('sp100.png')
# Convert it to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Plot it
plt.imshow(img)
plt.show()

# Split the image into the three colour channels
red, green, blue = cv2.split(img)

# Compose the image in the RGB colour space
img1 = cv2.merge([red, green, blue])

# Compose the image in the RBG colour space
img2 = cv2.merge([red, blue, green])

# Compose the image in the GRB colour space
img3 = cv2.merge([green, red, blue])

# Compose the image in the BGR colour space
img4 = cv2.merge([blue, green, red])

# Compose the image in the BGR colour space
img5 = cv2.merge([blue, green, blue])

# Compose the image in the BGR colour space
img6 = cv2.merge([blue, green, green])

# Create the collage
out1 = np.hstack([img1, img2])
out2 = np.hstack([img3, img4])
out3 = np.hstack([img5, img6])
out = np.vstack([out1, out2, out3])

# Plot the collage
plt.imshow(out)
plt.show()
plt.axis(False)