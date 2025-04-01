import cv2

def enhance_image(image_path, scale_factor=2):
    image = cv2.imread(image_path)
    upscaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    return upscaled_image
