import os
from PIL import Image, ImageOps
import numpy as np


def data_loader(train=True):
    parent_dir = './News/'
    if train:
        parent_dir += 'Train/'
    else:
        parent_dir += 'Test/'

    images = []

    for image_path in os.listdir(parent_dir):
        image = Image.open(f'{parent_dir}{image_path}')
        image = ImageOps.grayscale(image)
        image = np.array(image)
        images.append((image, image_path))
    return images
