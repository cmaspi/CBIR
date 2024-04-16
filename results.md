# SIFT
Used BoW approach

## News
retireval in top-10:

```
array([0.70939393, 0.74339695, 0.76051819, 0.7729221 , 0.78355403,
       0.79186322, 0.79890328, 0.80477   , 0.81042121, 0.81513853])
```

Augmentation:
```python
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Rotate(limit=20),
    A.GaussNoise(p=0.1),
])
```

## Paris

with `general` label in test images
```
array([0.5296875 , 0.4921875 , 0.47395833, 0.46484375, 0.455     ])
```

without `general` label
```
array([0.55693582, 0.52173913, 0.49689441, 0.48033126, 0.47039337])
```

## Oxford
```
array([0.36883629, 0.34615385, 0.32938856, 0.31508876, 0.29901381])
```