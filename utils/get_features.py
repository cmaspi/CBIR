import cv2
from typing import List
from tqdm import tqdm
import numpy as np

class SIFT:
    def __init__(self, mode='sift'):
        if mode == 'sift':
            self.descriptor_obj = cv2.SIFT_create()
            self.no_detect_return = np.zeros((1, 128))
        if mode == 'orb':
            self.descriptor_obj = cv2.ORB_create()
            self.no_detect_return = np.zeros((1, 32))
                    
    def __get_features__(self, image):
        kp, desc = self.descriptor_obj.detectAndCompute(image, None)
        if desc is not None:
            return desc
        else:
            return self.no_detect_return
    
    def get_features(self, images: List):
        features = []
        for img in tqdm(images):
            features.append(self.__get_features__(img))
        return features

