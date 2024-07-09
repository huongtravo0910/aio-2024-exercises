import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

img = mpimg.imread('module_2/week_1_numpy/dog.jpeg')
print(img)

# Q12: Change color image to grey image by lightness method


def cal_lightness(image):
    lightness = (np.max(image, axis=2) + np.min(image, axis=2)) / 2
    grayscale_image = np.stack([lightness] * 3, axis=-1)

    return grayscale_image


gray_img_01 = cal_lightness(img)
gray_img_01[0, 0]
print(gray_img_01[0, 0])

# plt.imshow(gray_img_01)
# plt.axis('off')  # Turn off axis labels
# plt.show()


# Q13: Change color image to grey image by average method

def cal_average(image):
    grayscale = np.mean(image, axis=2)

    grayscale_image = np.stack([grayscale] * 3, axis=-1)
    return grayscale_image


gray_img_02 = cal_average(img)  # Your Code Here
gray_img_02[0, 0]
print(gray_img_02[0, 0])

plt.imshow(gray_img_02)
plt.axis('off')  # Turn off axis labels
plt.show()

# Q14: Change color image to grey image by Luminosity method


def cal_luminosity(image):
    if image.shape[-1] == 4:
        image = image[..., :3]

    if image.dtype == np.uint8:
        image = image.astype(np.float32) / 255.0

    grayscale = 0.21 * image[..., 0] + 0.72 * \
        image[..., 1] + 0.07 * image[..., 2]

    grayscale_image = np.stack([grayscale] * 3, axis=-1)

    return grayscale_image


gray_img_03 = cal_luminosity(img)
gray_img_03[0, 0]
print(gray_img_03[0, 0])

# plt.imshow(gray_img_03)
# plt.axis('off')  # Turn off axis labels
# plt.show()
