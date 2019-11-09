## Sayısal Loto winner number predicting experiment with Machine Learning

**Project Name:** Sayisal_Loto_ML_experiment</br>
**Project Creator:** Hüseyin Emre Girgin</br>
**Project Publish Date:** November 2019</br>


#### Table of Contents:  
<!--ts-->
[What is Sayısal Loto](#what-is-sayısal-loto)  
[About](#about-the-project)  
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

## Results

![alt text](https://github.com/heg37/Sayisal_Loto_ML_experiment/blob/master/result_table.jpg "result table")</br>
The reults of the our Neural Network


