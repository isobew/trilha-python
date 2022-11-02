#Author: Karina Tiemi Kato
#Description by: Isabella Firmino
#Combinação das imagens

import numpy as np

#pacote de processamento de imagens
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

#achar diferença entre duas imagens
def find_difference(image1, image2):

    #verificando se os shapes são iguais e exibindo msg caso não seja
    assert image1.shape == image2.shape, "Specify 2 images with the same shape."

    #conversão pra tons de cinza das duas imagens de entrada, usando o modulo de color do scikit image
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)

    #usando o structural_similarity do módulo de metrics, fazemos a chamada passando as imagens com tons de cinza pra achar o score e difference_image
    #o score é um valor de 0 a 1, que diz o quanto as imagens são similares, e o difference_image é a imagem de diferença entre as duas imagens de entrada
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)

    #printando score e normalizando o difference_image, pra ficar mais fácil de identificar na imagem de diferença na hora que formos plotar 
    # (pra que se as imagens forem mt parecidas, não fique valores mt pequenos, por isso a normalização)
    print("Similarity of the images:", score)
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))
    return normalized_difference_image

def transfer_histogram(image1, image2):
    #função do módulo exposure do scikit image
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image