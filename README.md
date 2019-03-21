# cell-counting-from-images


## Testing Dataset
Our dataset contains folders with two componenets: 
- images with cells from microscopy
- csv file with columns: image, expected (expected is number of cells that we expect to have as result)
### Chinese Hamster Ovary Cells
link to source:  https://data.broadinstitute.org/bbbc/BBBC030/
link to data (images and csv file): https://drive.google.com/drive/folders/1AFtHcJ2UbZ1DNpQt8tUW7rLVt27fHUIH?usp=sharing
### Different kinds of cells(organisms, tissues, histology dies)
link to source: https://www.kaggle.com/c/data-science-bowl-2018/data
    used folder: /stage1_train/*
    script to process this data to proper structure in directory utils, named: process-kaggle-data.ipynb
link to data: https://drive.google.com/file/d/1eNtcULHZJpbDLY8g_AhNXbo6vLK-N7Wq/view?usp=sharing
###Synthetic cells
Each photo contains 300 objects.
link to source:  https://data.broadinstitute.org/bbbc/BBBC004/
link to data (images and csv file): https://drive.google.com/file/d/1-DcDU3SpUy1Co63K1vrg-4Ya6JooS4Fk/view?usp=sharing


## Requirenments

Python 3
Jupyter notebook
opencv2 version 4.00
pandas
matplotlib
seaborn

## How to use tests

1. Open file tests.ipynb in jupyter notebook
2. Read comments with clues 


## Bibliography:
1. https://www.researchgate.net/publication/258443282_Fast_automated_yeast_cell_counting_algorithm_using_bright-field_and_fluorescence_microscopic_images





