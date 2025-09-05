# Project Name : Diabetic-retinopathy-detection-CNN
  

# Problem statement :    
Diabetic Retinopathy is a disease with an increasing prevalence and the main cause of blindness among working-age population. The risk of severe vision loss can be significantly reduced by timely diagnosis and treatment. Systematic screening for DR has been identified as a cost-effective way to save health services resources. Automatic retinal image analysis is emerging as an important screening tool for early DR detection, which can reduce the workload associated to manual grading as well as save diagnosis costs and time. Many research efforts in the last years have been devoted to developing automated tools to help in the detection and evaluation of DR lesions.
We are interested in automating this predition using deep learning models.

# Dataset : [APOTS Kaggle Blindness dataset](https://www.kaggle.com/c/aptos2019-blindness-detection)      

# Solution :   
I am proposing Deep Learning classification technique using CNN pretrained model [resnet152](https://github.com/DhanushGowdaM/Diabetic-retinopathy-detection-CNN/blob/main/Resnet152.ipynb) to classify severity levels of DR ranging from 0 (NO DR) to 4 (Proliferative DR).   
This is a collaborative project of team of three where my main work is on developing, training and testing various CNN models along with some secondary work.
Deep learning looks promising because already various types of image classification tasks has been performed by various CNN's so, we can rely on DL pretrained models or we can modify some layers if we wish to :)    
A GUI based system has been made using Tkinter and used heidiSQL to maintain and store a list of predictions with their patient id and name (which is very risky , the reason we will get to it some time later).   
Twilio API have been used to Make SMS connectivity to patients possible in case they are not contactable or accesible (in that case we can also use mail).       

# Summary of Technologies used in this project :       
| Dev Env. | Framework/ library/ languages |
| ------------- | ------------- |
| Backend development  | PyTorch (Deep learning framework) |
| Frontend development | Tkinter (Python GUI toolkit) |
| Database connectivity | HeidiSQL (MySQL server) |
| Programming Languages | Python, SQL |
| API | Twilio cloud API|      

# Data visualization :     
Input data (raw) is like this -     
![visual1](https://github.com/DhanushGowdaM/Diabetic-retinopathy-detection-CNN/blob/main/GUI%20model%20images/Screenshot%202025-09-05%20092455.png)

# Resnet152 model summary :     
I have only shown below the main layers of resnet and each of the 'layer1', 'layer2', 'layer3' and 'layer4' contains various more layers.      

![mat](https://github.com/DhanushGowdaM/Diabetic-retinopathy-detection-CNN/blob/main/GUI%20model%20images/Screenshot%202025-09-05%20093843.png)      


# Getting started :       
[Click](https://github.com/DhanushGowdaM/Diabetic-retinopathy-detection-CNN/blob/main/GetStarted.md) here to get started locally on your system.

## Some snaps :     
![images/gui1.JPG](https://github.com/DhanushGowdaM/Diabetic-retinopathy-detection-CNN/blob/main/GUI%20model%20images/Screenshot%20(38).png)
![images/gui2.JPG](https://github.com/DhanushGowdaM/Diabetic-retinopathy-detection-CNN/blob/main/GUI%20model%20images/Screenshot%20(39).png)
![images/gui3.JPG](https://github.com/DhanushGowdaM/Diabetic-retinopathy-detection-CNN/blob/main/GUI%20model%20images/Screenshot%20(40).png)
![images/sms.JPG](https://github.com/DhanushGowdaM/Diabetic-retinopathy-detection-CNN/blob/main/GUI%20model%20images/Screenshot%20(41).png)

 
 # Future Prospect :    
 * My next goal is to develop this into WebApp (probably using some light weight model as resnet models are heavy).   
 * Next goal will be using encryption techniques to achieve not only high accuracy but also high level of privacy in terms of differentially private basis and use technqiues such as Federated learning and Secure Multi party computation for privacy preserving deep learning classification.
 * Some ideas for concurrency control has to be implemented properly using some kind of locks defined in MySQL so that multiple users can use the system at the same time when deployed on web.
 (Otherwise, locally you can run the executable file multiple times to open and run the GUI and it works fine).      
 * Reducing TYPE-II error (false negatives) as this metric is really useful in Healthcare domain.   

[Note : The training files in this repo is only shown after final training as it took around more than 100 epochs to reach 97% accuracy and a lot of compute power and time.]     


⭐️ this Project if you liked it !
