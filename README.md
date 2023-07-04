# ALZHIMERS DISEASE DETECTION & CLASSIFICATION:
# ABSTRACT: 
The accurate diagnosis of Alzheimer’s disease (AD) plays an important role in patient treatment, especially at the disease’s early stages, because risk awareness allows the patients to undergo preventive measures even before the occurrence of irreversible brain damage. Although many recent studies have used computers to diagnose AD, most machine detection methods are limited by congenital observations. AD can be diagnosed-but not predicted-at its early stages, as prediction is only applicable before the disease manifests itself.Deep Learning (DL) has become a common technique for the early diagnosis of AD. Here, we briefly
review some of the important literature on AD and explore how DL can help researchers diagnose the disease
at its early stages.

# Installation:
 1. Anaconda 2021
 2. Required Libaries:
    numpy==1.20.3
    matplotlib==3.4.3
    tensorflow==2.8.0
    keras==2.8.0
    opencv-python==4.5.5.62

# Data Collection:  
    Dataset collected from Kaggle website:  source link: https://www.kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images

# Project Descriptions:
       No.of sample Images collected with classes: MildDemented = 717
                                                   ModerateDemented = 52
                                                   Non Demented = 2560
                                                   Very Mild Demented = 1792
                                                
Collected Samples Images are like Unbalanced, so i have done Data Augumentation Method with Keras.preprocessing to increase the sample Images.

After Augumentation Method the Sample Images MildDemented = 1739
                                                   ModerateDemented = 1421
                                                   Non Demented = 1753
                                                   Very Mild Demented = 1747

# Model Training:
In this Model I have used Transfer Learning Method (InceptionV3):
With Sample Images I have trained the Images with Batch_size=8 Epochs=50 and attained Training accuracy is 87% and Losses is 0.34%
and Tested with same Epochs attained Testing Accuracy is 85% and Lossess is 0.34%

# Model Deployment : (Flask)

To run the app: Go to cmd (command prompt)

run python app.py

and upload the testing Images to check the Model detection... 



