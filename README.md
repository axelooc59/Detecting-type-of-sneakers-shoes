# Detecting Nike type of sneakers 

Computer vision for detecting type of sneakers shoes (only trained for brand Nike)




**Aim of this project :**

As a sneakers addict, it is really easy for me to guess the type of shoes I am looking.
But for instance, when I show picture to my relatives they cannot differentiate dunk with jordan.
  
Therefore my project of computer vision aim to tell you what type of shoes it is by giving him a picture in input. We would like to have an accuracy of 80 % percentage.

Here a **concrete example** :  

You choose this picture:

<img src="https://github.com/axelooc59/Detecting-type-of-sneakers-shoes/blob/main/mocha.png" alt="drawing" width="200"/>

It will return his types which is *Jordan 1 High*.

My program will support the following type of shoes:
* Jordan 1 High
* Jordan 1 Mid
* Jordan 1 low
* Jordan 3
* Jordan 4
* Dunk low (classic shape)
* Dunk high

As a beginner in machine learning and in order to make this project easier and possible the only accepted picture is like the below one.   
Namely the shoe is oriented to the left and on a white background.

## Step of this project 
This project have three main step:
1. Collect data to train our model
2. Pre process the data collected
3. Create our model by giving him our data


### 1. Collecting data 
(file [collecting_data.ipynb](https://github.com/axelooc59/Detecting-type-of-sneakers-shoes-by-ML-/blob/master/CV_SNKRS/collecting_data.ipynb))  
In order to collect data we will scrap sneakers picture of the website [restocks.net](https://restocks.net), in that way we will get easily labeled data.
  
For that we will use the library *requests* of python and a little of javascript to get link of picture.

We sort each picture into their correspondants folder.

See the code in *collecting_data.ipynb*

We were able to collect a total of 725 pictures. This is not a lot to train a deep neural network. That's why I had chosen previously to use the same type pattern of sneakers pictures to make this training possible.

### 2. Preprocessing data 
(file [pre_processes.ipynb](https://github.com/axelooc59/Detecting-type-of-sneakers-shoes-by-ML-/blob/master/CV_SNKRS/pre_procceses.ipynb))  

For preprocess our data we don't have a lot to do. I have resive all the picture to 200x200 pixel size and divide each image per 256 in order to have value between 0 and 1 for our deep network.  
+ A 1 mean a black pixel, and a zero mean a write pixel.

I have seperated the Dataset in a training set (80%) and a validation set(20%).

### 3. Writing our deep neural Network
(file [pre_processes.ipynb](https://github.com/axelooc59/Detecting-type-of-sneakers-shoes-by-ML-/blob/master/CV_SNKRS/pre_procceses.ipynb))  
I have created Convolutional neural network (CNN) which is really appropriate for treating picture.
To do so I have used the library keras of **TensorFlow**.

I managed to hit an accurancy of 82% on the validation set.

Below the result of prediction by my neural network on the validation set :  







