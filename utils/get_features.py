import cv2
from typing import List
from tqdm import tqdm

class SIFT:
    def __init__(self, mode='sift'):
        if mode == 'sift':
            self.descriptor_obj = cv2.SIFT_create()
        if mode == 'orb':
            self.descriptor_obj = cv2.ORB_create()
                    
    def __get_features__(self, image):
        kp, desc = self.descriptor_obj.detectAndCompute(image, None)
        return desc
    
    def get_features(self, images: List):
        features = []
        for img in tqdm(images):
            features.append(self.__get_features__(img))
        return features

