# Object Detection model using the ImageAI library

## Requirements :

1. Python   
2. Some packages -> tensorflow, numpy, scipy, opencv, pillow, matplotlib, h5py, keras and  
3. Obviously -> the ImageAI library (*https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl)*  

### here's HOW 

* Install python from *https://www.python.org/downloads/*  
* For the packages you might make use of the "pip install package_name" statement or simply create an Anaconda environment with  
          ```
          conda create -n retinanet python=3.6 anaconda
          ```  
  Activate the environment and install the necessary packages. Easy as that  
          ```
          source activate retinanet  
          conda install tensorflow numpy scipy opencv pillow matplotlib h5py keras  
          ```
* Install the ImageAI library using  
          ```
          pip install *https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl*
          ```



## Execution :

We'll use the pre-trained RetinaNet-based model (why? its a quick proect)  
Download the model from *https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5* and save in cwd.  
that's it, run the script (python script.py) with proper image name in script. Model runs and saves the image file with detected objects.  



## Observations :
The 'image.png' worked well and model identified the solo pedestrian

![image](https://user-images.githubusercontent.com/23148500/42644404-26839316-8619-11e8-9ff7-977b1b4b2068.png)
![image_new](https://user-images.githubusercontent.com/23148500/42644420-34db584a-8619-11e8-8acb-2940b2e332c9.png)

Then I plugged the famous(or not apparently) Abbey Road picture 
Turns out the model could identify only two pedestrians leaving behind John Lennon and George Harrison  

![image2](https://user-images.githubusercontent.com/23148500/42644421-35157502-8619-11e8-90a5-3f94b864e56c.jpg)
![image2_new](https://user-images.githubusercontent.com/23148500/42644422-354e750a-8619-11e8-911a-e3f752155ebc.jpg)  
Maybe the grooming ? Anyway that's good enough for a start  

**BEATLES** forever !
