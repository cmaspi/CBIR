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

```
array([0.51875   , 0.48671875, 0.47291667, 0.45625   , 0.4471875 ])
```

RANSAC
```
array([0.575     , 0.5375    , 0.51822917, 0.50039062, 0.486875  ]),
```

## Oxford
```
array([0.3234714 , 0.32051282, 0.2991453 , 0.28648915, 0.27810651])
```

RANSAC
```
array([0.42209073, 0.37968442, 0.34319527, 0.32149901, 0.30374753]), 
```