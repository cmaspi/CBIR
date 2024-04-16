import os
from PIL import Image, ImageOps
import numpy as np
from tqdm import tqdm


def data_loader():
    base_directory = os.path.dirname(__file__)
    parent_dir = base_directory + '/paris/'
    images = []
    image_labels = []
    for child_dir in tqdm(os.listdir(parent_dir)):
        for image_name in tqdm(os.listdir(parent_dir+child_dir), leave=False):
            image = Image.open(f'{parent_dir}{child_dir}/{image_name}')
            image = ImageOps.grayscale(image)
            image = np.array(image)
            images.append(image)
            image_labels.append(child_dir)
    return images, image_labels
