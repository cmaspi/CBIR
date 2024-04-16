# SIFT
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