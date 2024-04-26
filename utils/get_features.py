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
                    
    def __get_features__(self, image, ret_keypoints=False):
        kp, desc = self.descriptor_obj.detectAndCompute(image, None)
        if desc is None:
            desc = self.no_detect_return
        if ret_keypoints:
            return kp, desc
        else:
            return desc
    
    def get_features(self, images: List, return_keypoints):
        features = []
        if return_keypoints:
            keypoints = []
        for img in tqdm(images):
            ret = self.__get_features__(img, return_keypoints)
            if return_keypoints:
                kp, d = ret
                keypoints.append(kp)
            else:
                d = ret
            features.append(d)
        if return_keypoints:
            return keypoints, features
        return features

