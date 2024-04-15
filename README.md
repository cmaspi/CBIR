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

