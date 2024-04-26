"""
Implements the RANSAC algorithm using Lowe's ratio, it uses USAC_MAGSAC
instead of RANSAC.
"""

import cv2
import numpy as np
from typing import List
from multiprocessing import Process, Array


def ransac_sift(d1, d2, kp1, kp2):
    if kp1 is None or kp2 is None:
        return 0
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(d1, d2, k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)
    if len(good) < 4:
        return 0

    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.USAC_MAGSAC, 5.0)
    return mask.sum()


def rasnac_for_multiprocessing(method, arr, index, *args):
    res = method(*args)
    arr[index] = res


def ransac_sift_multiprocessing(d1, d2l: List, kp1, kp2l: List):
    processes = []
    n = len(d2l)
    arr = Array('i', [0] * n)
    for idx, (d2, kp2) in enumerate(zip(d2l, kp2l)):

        p = Process(target=rasnac_for_multiprocessing,
                    args=(ransac_sift, arr, idx, d1, d2, kp1, kp2))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    return np.array(arr)
