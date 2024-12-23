## Importing Libraries
import pandas as pd
import numpy as np
import matplotlib as plt

## Read the CSV Files of the Dataset (Training & Testing)
training_set = pd.read_csv('Dataset/fashion-mnist_train.csv')
test_set = pd.read_csv('Dataset/fashion-mnist_test.csv')

## Training Data Pre-Processing
x_train = training_set.iloc[:, 1:]
y_train = training_set.iloc[:, 1:]

## Test Data Pre-Processing
## Ignore the Column - Label - so the values are from 1-784 rather than 0-784 as pd uses 0-based indexing i think 
x_test = test_set.iloc[:, 1:]
y_test = test_set.iloc[:, 1:]

## Normalise Pixel Values (Force values to be between 0-1) 
x_train = x_train/255
y_train = y_train/255

print(x_train.shape)
print(y_test.shape)

