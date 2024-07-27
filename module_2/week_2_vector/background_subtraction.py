
import numpy as np
import cv2


# (a) Resize các ảnh đầu vào về cùng kích thước:
bg1_image = cv2.imread("module_2/week_2_vector/GreenBackground.png", 1)
ob_image = cv2.imread("module_2/week_2_vector/Object.png", 1)
bg2_image = cv2.imread("module_2/week_2_vector/NewBackground.jpg", 1)

height, width, _ = bg2_image.shape
ob_image = cv2.resize(ob_image, (width, height))
bg1_image = cv2.resize(bg1_image, (width, height))
bg2_image = cv2.resize(bg2_image, (width, height))

# (b) Xây dựng hàm compute_difference():


def compute_difference(bg_img, input_img):
    difference_single_channel = cv2.absdiff(input_img, bg_img)
    difference_single_channel = cv2.cvtColor(
        difference_single_channel, cv2.COLOR_BGR2GRAY)
    return difference_single_channel

# (c) Xây dựng hàm compute_binary_mask():


def compute_binary_mask(difference_single_channel):
    _, fg_mask = cv2.threshold(
        difference_single_channel, 0, 255, cv2.THRESH_BINARY)
    return fg_mask


# (d) Xây dựng hàm replace_background():
def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(
        bg1_image,
        ob_image
    )
    cv2.imwrite('module_2/week_2_vector/difference_single_channel.png',
                difference_single_channel)

    binary_mask = compute_binary_mask(difference_single_channel)
    binary_mask = cv2.cvtColor(
        binary_mask, cv2.COLOR_GRAY2BGR)
    cv2.imwrite('module_2/week_2_vector/binary_mask.png', binary_mask)

    output = np.where(binary_mask == 255,
                      ob_image,
                      bg2_image)
    return output


# Save or display the final output
final_output = replace_background(bg1_image, bg2_image, ob_image)
cv2.imwrite('module_2/week_2_vector/final_output.png', final_output)
