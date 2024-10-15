import cv2

def load_image(filepath):
    """Carrega uma imagem a partir do caminho especificado"""
    return cv2.imread(filepath)

def save_image(image, filepath):
    """Salva a imagem no caminho especificado"""
    cv2.imwrite(filepath, image)
