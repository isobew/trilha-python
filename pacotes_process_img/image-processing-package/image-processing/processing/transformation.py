#Author: Karina Tiemi Kato
#transformação para uma imagem apenas

from skimage.transform import resize

#passando imagem e proporção, a ideia é utilizar quando forem imagens mt grandes, p diminuí-las
def resize_image(image, proportion):

    #proporção de 0 a 1, lançando msg se não for de 0 a 1
    assert 0 <= proportion <=1, "Specify a valid proportion between 0 and 1."

    #pegando da imagem o shape 0 e 1 e multiplicando pela proporção pra pegar a altura e largura depois de aplicada a proporção que queremos
    #round usado para ser um valor inteiro, pois precisa ser passado como inteiro na image_resized
    height = round(image.shape[0]*proportion)
    width = round(image.shape[1]*proportion)

    #função do transform, passando valor de largura e altura, e imagem que queremos fazer resize
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized