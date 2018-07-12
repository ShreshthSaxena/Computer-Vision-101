# Object Detection model using the ImageAI library

## Requirements :

1. Python   
2. Some packages -> tensorflow, numpy, scipy, opencv, pillow, matplotlib, h5py, keras and  
3. Obviously -> the ImageAI library (*https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl)*  

### here's HOW 

* Install python from *https://www.python.org/downloads/*  
* For the packages you might make use of the "pip install package_name" statement or simply create an Anaconda environment with  
          '''
          conda create -n retinanet python=3.6 anaconda
          '''
  Activate the environment and install the necessary packages. Easy as that  
          source activate retinanet
          conda install tensorflow numpy scipy opencv pillow matplotlib h5py keras
* Install the ImageAI library using  
          pip install *https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl*



## Execution :
We'll use the pre-trained RetinaNet-based model (why? its a quick proect)
Download the model from *https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5* and save in cwd.
thats it, run the script (python script.py) with proper image name in script. Model runs and saves the image file with detected objects.



## Observations :
The 'image.png' worked well and model identified the solo pedestrian (check 'image_new.png')

Then I plugged the famous(or not apparently) Abbey Road picture ('image1.jpg')
Turns out the model could identify only two pedestrians leaving behind John Lennon and George Harrison ('image1_new.jpg')
Maybe the grooming ? Anyway 50% accuracy is good enough for a start 
**BEATLES** forever !
