# Uni-YOLO: Large Model Guided YOLO for Robotic Universal Detection in the Open World
Xudong Wang, Xi’ai Chen *, Huijie Fan, Yandong Tang, Yang Cong, Zhi Han <br />
 <br />
The State Key Laboratory of Robotics, Shenyang Institute of Automation, Chinese Academy of Sciences, and also University of Chinese Academy of Sciences (UCAS). (e-mail: wangxudong@sia.cn).
## Our work 

<p float="left">
  &emsp;&emsp; <img src="./f2.png" width="900" />
</p>

In this work, we propose Uni-YOLO, a universal object detector for robots that has the ability to detect any object in the open world.

<p float="left">
  &emsp;&emsp; <img src="./f7.png" width="900" />
</p>

## Dependencies
* Python 3.8
* PyTorch 1.8.1 + cu111
* torchvision 0.9.1 + cu111
* numpy
* opencv-python
* skimage
* hiddenlayer
* matplotlib
* PIL
* math
* os
## Architecture
model.py: The definition of the model class.

utils.py: Some tools for network training and testing.

data.py: Preparation tools for the training dataset.

test.py: Quick dehazing test for hazy images.

testall.py: Dehazing test for all hazy images dataset.

train.py: Training the dehazing model by supervised learning.

SemiStrain.py: Training the dehazing model by Semi-supervised learning in specific dataset.


## Test
1. Please put the images to be tested into the ``test_images`` folder. We have prepared the images of the experimental results in the paper.
2. Please run the ``test.py``, then you will get the following results:

