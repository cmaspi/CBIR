# SIFT
Used BoW approach

## News
retireval in top-10:

```
[0.75975976, 0.8038038 , 0.81881882, 0.82782783, 0.83483483]
```

RANSAC
```
[0.77577578, 0.82382382, 0.84284284, 0.84784785, 0.85485485]
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