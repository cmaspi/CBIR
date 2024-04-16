# CBIR

# Datasets
## News
Download the dataset using

```shell
kaggle datasets download -d troooonnn/news-images-dataset
unzip news-images-dataset.zip
mkdir Datasets/News
mv DATA/images\ \(1\)/ Datasets/News/Train
rm Datasets/News/Train/1400070516181726323700473.jpg # empty image
```

## Paris and Oxford
Download the datasets using
```shell
kaggle datasets download -d skylord/oxbuildings
```

### Paris
Organise Paris inside Datasets directory as follows

```
Paris/
└── paris
    ├── defense
    ├── eiffel
    ├── general
    ├── invalides
    ├── louvre
    ├── moulinrouge
    ├── museedorsay
    ├── notredame
    ├── pantheon
    ├── pompidou
    ├── sacrecoeur
    └── triomphe    
```

Remove the following corrupted files

```shell
rm louvre/paris_louvre_000146.jpg
rm louvre/paris_louvre_000136.jpg
rm moulinrouge/paris_moulinrouge_000422.jpg
rm museedorsay/paris_museedorsay_001059.jpg
rm notredame/paris_notredame_000188.jpg
rm pantheon/paris_pantheon_000284.jpg
rm pantheon/paris_pantheon_000960.jpg
rm pantheon/paris_pantheon_000974.jpg
rm pompidou/paris_pompidou_000195.jpg
rm pompidou/paris_pompidou_000196.jpg
rm pompidou/paris_pompidou_000201.jpg
rm pompidou/paris_pompidou_000467.jpg
rm pompidou/paris_pompidou_000640.jpg
rm sacrecoeur/paris_sacrecoeur_000299.jpg
rm sacrecoeur/paris_sacrecoeur_000330.jpg
rm sacrecoeur/paris_sacrecoeur_000353.jpg
rm triomphe/paris_triomphe_000662.jpg
rm triomphe/paris_triomphe_000833.jpg
rm triomphe/paris_triomphe_000863.jpg
rm triomphe/paris_triomphe_000867.jpg
```

### Oxford
use this script to put the images into directories

```python
import os


for file_name in os.listdir('./'):
    label = file_name[:-11]
    os.makedirs(f'./{label}/', exist_ok=True)
    os.system(f'mv {file_name} {label}/')
```

