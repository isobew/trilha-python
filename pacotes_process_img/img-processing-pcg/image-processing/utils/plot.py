#Author: Karina Tiemi Kato

import matplotlib.pyplot as plt

#plotar única imagem
def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

#plotar resultado de combination e transformation, aumentando número de colunas de acordo com o tamanho de args e depois tendo coluna de resultado
def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplot(nrows=1, ncols = number_images, figsize=(12,4))
    names_lst = ['image {}'.format(i) for i in range(1, number_images)]
    names_lst.append('Result')
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

#passa uma imagem para plotar o histograma, com 3 colunas para R, G e B
def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols = 3, figsize=(12,4), sharex=True, sharey=True)
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} histogram'.format(color.title()))
        ax.hist(image[:, :, index].ravel(), bins = 256, color = color, alpha = 0.8)
    fig.tight_layout()
    plt.show()