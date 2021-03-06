# Poker Prediction Model (CS419 Project)

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
- [poker_prediction.ipynb](https://colab.research.google.com/drive/1flWsONo_E0LKh4euKR9dUmADwLQrVhoz?usp=sharing)

The `poker-hand-testing.csv` and `poker-hand-training-true.csv` files are generated from `poker-hand-testing.data` and `poker-hand-training-true.csv` files respectively.

The `generate_csv.py` file is used to convert `.data` files to `.csv` files. It can be used as 
```
python generate_csv.py [filename]
```

For, example
```
python generate_csv.py poker-hand-testing.data
```
This will return a `poker-hand-testing.csv` file which is used in our model.

The `poker_prediction.ipynb` file contains all the codes for reading, analysing and predicting data. It also displays results of accuracy and precision of the model. The google colab notebook can be found here (https://colab.research.google.com/drive/1flWsONo_E0LKh4euKR9dUmADwLQrVhoz?usp=sharing)

The contributors and work distribution:
- Rudraksh Kuchiya (20D110021): Formulating the model, writing the python notebook, fitting the model and generating results; compiling the github repo and readme file, riting and compiling report on Latex.
- Aarya Chaudhari (20D110002): Writing the report and presentation
- Muskan Bhutra (200040085): Writing the report and presentation
- Raghav Rander (200040113): Writing the report and presentation
- Utkarsh Jindal (200070086): Writing the report and presentation
