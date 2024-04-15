import os
from PIL import Image, ImageOps
import albumentations as A
import numpy as np
from tqdm import tqdm



transform = A.Compose([
    # A.HorizontalFlip(p=0.5),
    # A.RandomBrightnessContrast(p=0.2),
    # A.Rotate(limit=20),
    # A.GaussNoise(p=0.1),
])


base_directory = os.path.dirname(__file__)
train_dir = base_directory+'/Train/'

def gen_test_data():
    for image_name in tqdm(os.listdir(train_dir)):
        image = Image.open(train_dir + image_name)
        image = ImageOps.grayscale(image)
        image = np.array(image)
        transformed_image = transform(image=image)
        yield transformed_image, image_name
