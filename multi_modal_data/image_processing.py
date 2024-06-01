import cv2
import numpy as np

def resize_image(image, size):
    return cv2.resize(image, size)

def normalize_image(image):
    return image / 255.0

def apply_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_blur(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

if __name__ == "__main__":
    pass
