import os
from PIL import Image, ImageOps
import numpy as np
from tqdm import tqdm


def data_loader():
    base_directory = os.path.dirname(__file__)
    parent_dir = base_directory + '/Train/'

    images = []
    image_names = []
    for image_name in tqdm(os.listdir(parent_dir)):
        image = Image.open(f'{parent_dir}{image_name}')
        image = ImageOps.grayscale(image)
        image = np.array(image)
        images.append(image)
        image_names.append(image_name)
    return images, image_names
