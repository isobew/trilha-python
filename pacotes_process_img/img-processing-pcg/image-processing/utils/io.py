#Author: Karina Tiemi Kato
#leitura e escrita de imagem usando scikit image io

from skimage.io import inread, insave

def read_image(path, is_gray = False):
    image = inread(path, as_gray = is_gray)
    return image

def save_image(image, path):
    insave(path, image)