## Sayısal Loto winner number predicting experiment with Machine Learning

**Project Name:** Sayisal_Loto_ML_experiment</br>
**Project Creator:** Hüseyin Emre Girgin</br>
**Project Publish Date:** November 2019</br>


#### Headers:
<!--ts-->
[What is Sayısal Loto](#what-is-sayısal-loto)</br>
[About](#about-the-project)</br>
[Our Neural Network's summaries](our-neural-networks-summaries)</br>
[Results](#results)</br>
[Conclusion](#conclusion)</br>
<a name="headers"/>
<!--te-->

## What is Sayısal Loto
Sayısal Loto is a kind of lottery from Turkey. It has started in 1996[*](https://tr.wikipedia.org/wiki/Say%C4%B1sal_Loto). For win, you must predict 6 number string from numbers of 1 to 49.

## About the project
In this project we have try to find connection between lottery date and Sayisal Loto winner numbers.</br>
#### Here the steps of the our project:
1. **Get a dataset**</br>
   I made researches for find all draw's table. So I find [a webpage](http://lotobayisi.com/Sayisal-Butun-Veriler.aspx) for get the data.
2. **We turned it to array as a json file**</br>
3. **We edited, seperated and saved files for dataset**</br>
   I did this step with lib_of_the_sayisalloto.py file. So if you want yours you can use this Python file.</br>
   We create a train and test datasets for NN. We picked randomly 100 samples. Then, we turned it to .npz file for save.
4. **Finalizing**</br>
   In the final, we are training our dataset with Sequential model. You can find codes in trainer_of_loto.py file.
 
As you see this is a classical train method for a NN.

### Training Method:

I have tried many method for training statement but this is best result I could find. So If you have a better idea feel free to try and share with us.
I made my trainings on Google Colab because of my computers hardwares and Colab's speed. I have tried different layers and neurons and I saved best resoult as an .h5 file.

I created a dataset. (as you see the .npz file's name has a "3", so as you understand it is a version 3 of my datasets.) I gave 4 inputs as an 2x2 matrix and I get 1 output.
I tried 4 inputs and 6 outputs model but it does not worked efficiently so I found this.

**We have a input data matrix as like:**</br>
[ "Draw Week"   "Day"  ]</br>
[   "Month"     "Year" ]</br>

**and we have a output as:**</br>["Number"]

## Our Neural Network's results
`````
Model loto_model_num1.h5
Model: "sequential_5"
loto_model_.summary()
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
flatten_5 (Flatten)          (None, 4)                 0         
_________________________________________________________________
dense_10 (Dense)             (None, 128)               640       
_________________________________________________________________
dense_11 (Dense)             (None, 31)                3999      
=================================================================
Total params: 4,639
Trainable params: 4,639
Non-trainable params: 0
_________________________________________________________________
`````
`````
Model loto_model_num2.h5
Model: "sequential_14"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
flatten_14 (Flatten)         (None, 4)                 0         
_________________________________________________________________
dense_43 (Dense)             (None, 64)                320       
_________________________________________________________________
dense_44 (Dense)             (None, 512)               33280     
_________________________________________________________________
dense_45 (Dense)             (None, 256)               131328    
_________________________________________________________________
dense_46 (Dense)             (None, 41)                10537     
=================================================================
Total params: 175,465
Trainable params: 175,465
Non-trainable params: 0
_________________________________________________________________
`````
`````
Model loto_model_num3.h5
Model: "sequential_25"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
flatten_25 (Flatten)         (None, 4)                 0         
_________________________________________________________________
dense_81 (Dense)             (None, 64)                320       
_________________________________________________________________
dense_82 (Dense)             (None, 128)               8320      
_________________________________________________________________
dense_83 (Dense)             (None, 512)               66048     
_________________________________________________________________
dense_84 (Dense)             (None, 45)                23085     
=================================================================
Total params: 97,773
Trainable params: 97,773
Non-trainable params: 0
_________________________________________________________________
`````
`````
Model loto_model_num4.h5
Model: "sequential_26"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
flatten_26 (Flatten)         (None, 4)                 0         
_________________________________________________________________
dense_85 (Dense)             (None, 64)                320       
_________________________________________________________________
dense_86 (Dense)             (None, 128)               8320      
_________________________________________________________________
dense_87 (Dense)             (None, 512)               66048     
_________________________________________________________________
dense_88 (Dense)             (None, 48)                24624     
=================================================================
Total params: 99,312
Trainable params: 99,312
Non-trainable params: 0
_________________________________________________________________
`````
`````
Model loto_model_num5.h5
Model: "sequential_6"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
flatten_6 (Flatten)          (None, 4)                 0         
_________________________________________________________________
dense_24 (Dense)             (None, 64)                320       
_________________________________________________________________
dense_25 (Dense)             (None, 256)               16640     
_________________________________________________________________
dense_26 (Dense)             (None, 512)               131584    
_________________________________________________________________
dense_27 (Dense)             (None, 49)                25137     
=================================================================
Total params: 173,681
Trainable params: 173,681
Non-trainable params: 0
_________________________________________________________________
``````
``````
Model loto_model_num6.h5
Model: "sequential_30"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
flatten_30 (Flatten)         (None, 4)                 0         
_________________________________________________________________
dense_101 (Dense)            (None, 64)                320       
_________________________________________________________________
dense_102 (Dense)            (None, 256)               16640     
_________________________________________________________________
dense_103 (Dense)            (None, 512)               131584    
_________________________________________________________________
dense_104 (Dense)            (None, 50)                25650     
=================================================================
Total params: 174,194
Trainable params: 174,194
Non-trainable params: 0
_________________________________________________________________
``````
## Results
![alt text](https://github.com/heg37/Sayisal_Loto_ML_experiment/blob/master/result_table.jpg "result table")</br>
The reults of the our Neural Network

![alt text](https://github.com/heg37/Sayisal_Loto_ML_experiment/blob/master/testtrain%20graph.png "testtrain% graph")</br>
This has calculated from (test accuracy)/(train accuracy)

![alt text](https://github.com/heg37/Sayisal_Loto_ML_experiment/blob/master/releation%20graph.png "testtrain% graph")</br>
In the results, I find a inverse relation between train and test graphics

## Conclusion
We have tried to find a releation in lottery. I want to focus on 1st ball since best result. So, we can ask with this work if everythings happening randomy how can a Machine find %11 true results. 

Maybe this work shows nothing truely but you can look this project as an experiment. Please feel free to comment about this work and try your new Neural Network, and enjoy.
