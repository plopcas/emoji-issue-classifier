# Emoji Issue Classifier Training

This folder contains the training script and data for training an emoji issue classifier using machine learning.

## Prerequisites

- Python 3.x
- NLTK library (for data augmentation)
- WordNet corpus (part of NLTK)

## Installation

1. Install the required dependencies:

```
pip3 install -r requirements.txt
```
   
2. Download the WordNet corpus:

```
python wordnet.py
```

This will download the WordNet corpus, which is required for data augmentation using synonym replacement.

## Usage

1. To train the emoji issue classifier, follow these steps:

2. Add or update the labeled training data in the labeled_data list in the train.py file. Include relevant issue descriptions and their corresponding labels.

3. Run the training script:

```
python train.py
```

This will train the classifier using the labeled data, perform data augmentation using synonym replacement, and save the trained model as `model.pkl`.

The trained model can be used for predicting the labels of new issue descriptions.

Note: It is recommended to periodically update and refine the labeled training data to improve the classifier's accuracy.