import os
from PIL import Image, ImageOps
import albumentations as A
import numpy as np
from tqdm import tqdm


transform = A.Compose([
    A.RandomCrop(width=256, height=256),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Rotate(limit=40),
    A.GaussianNoise(p=0.2),
])


if not os.path.exists('./News/Test/'):
    os.makedirs('./News/Test/')

train_dir = './News/Train/'
test_dir = './News/Test/'
for image_path in tqdm(os.listdir(train_dir)):
    image = Image.open(train_dir + image_path)
    image = ImageOps.grayscale(image)
    image = np.array(image)
    transformed_image = transform(image)
    image = Image.fromarray(transformed_image)
    image.save(test_dir+image_path)

