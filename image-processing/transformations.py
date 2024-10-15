import cv2

def resize_image(image, width, height):
    """Redimensiona a imagem para uma largura e altura específicas"""
    return cv2.resize(image, (width, height))

def rotate_image(image, angle):
    """Roda a imagem pelo ângulo especificado"""
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, matrix, (w, h))