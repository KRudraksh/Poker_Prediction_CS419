# Poker Prediction Model CS419 Project

This repository contains a Deep Neural Networks model for predicting hands in poker. 

#### Required libraries:
- [keras.models](https://phoenixnap.com/kb/how-to-install-keras-on-linux)
- [keras.layers](https://phoenixnap.com/kb/how-to-install-keras-on-linux)
- numpy
- mathplotlib
- math

This repo contains following files:
- poker-hand-testing.data
- poker-hand-training-true.data
- poker-hand-testing.csv
- poker-hand-training-true.csv
- generate_csv.py
- poker_prediction.ipynb

The `generate_csv.py` file is used to convert `.data` files to `.csv` files. It can be used as 
```
python generate_csv.py [filename]
```

For, example
```
python generate_csv.py poker-hand-testing.data
```
This will return a `poker-hand-testing.csv` file which is used in our model.

The `poker_prediction.ipynb` file contains all the codes for reading, analysing and predicting data. It also displays results of accuracy and precision of the model.

The contributors are:
- Rudraksh Kuchiya 20D110021
- AArya Chaudhari 20D110002
- Muskan Bhutra
- Raghav Rander
- Utkarsh Jindal
