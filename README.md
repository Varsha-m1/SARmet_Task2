# SARmet_Task2

## Objective: Utilize OpenCv skills to complete the given tasks

###### Using cameras, Writing into a video file, processing on video frames and edge detection. 

Hope you learnt the bare basics of OpenCv with SARmet_Task1. 
Let's step up. Here's your task 2. 

Concepts you need to know: 
1. [Basic relationship between Pixels](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=16&ved=2ahUKEwi0w57BmPzeAhWKXisKHYKvAD8QFjAPegQIARAC&url=http%3A%2F%2Felearning.uokerbala.edu.iq%2Fmod%2Fresource%2Fview.php%3Fid%3D8510&usg=AOvVaw1KPO-RUI3yTVDuHbkrDtuE)

2. [Morphological Transformations](https://docs.opencv.org/3.4/d9/d61/tutorial_py_morphological_ops.html)  

3. Edge Detection Algorithms
    * [Sobel](https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/sobel_derivatives/sobel_derivatives.html)
    * [Canny Edge Detector](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html)
 
## Your tasks

1. Access your Laptop Webcam with OpenCv. Capture a **5 sec video** write into a video file. During the capture, also **display in real time** the feed being captured. 

2. During the display of the real time feed, you will observe a lag in display of this real time feed. Suggest methods to overcome this lag and implement one of them. 

3. Find the image named **720x1280.jpg** in the repository. Perform rotation around the X Axis and Y Axis and save as two different images. Thereafter, **subtract** these two images and save the resultant image.  

4. Use the orginal **720x1280.jpg** image and programmatically crop the image to 240x1280 pixels. Use the resultant cropped image to perform edge detection with any of the algorithms you prefer. (Mention the algorithm you use) 

5. Perform **Canny Edge Detection** on the orginal **720x1280.jpg** image and perform the following

    * Set the L2Gradient in the Canny Edge detector to **True** and save the result.
    * Use **5** different minimum and maximum thresholds and save the these 5 images. 
    * Set the Sobel Aperture size in the Canny Edge Detector to 1,3,5 and 7 and save these 4 images. 

## How to save your answers
1. Create a **folder with your name**.

2. Create **subfolders for each task**.

    * Task one - save the program and the 5 sec video you captured. (1 program, 1 video file)
    * Task two - save the program the video without the lag (1 program, 1 video file) 
    * Task three - save the program, the image rotated about the X axis, Y axis and the resultant difference image (1 program, 3 images)
    * Task four - save the program, cropped image, edge detected image (1 program, 2 images)
    * Task five - save the program, L2Gradient image, 5 different thresholded images, 4 Sobel operator image (1 program, 10 images)
  

Permission to collaborate for this repository has been sent by mail. 
Save your Answer programs should be saved in a **folder with your name** and uploaded to the repository.


Happy Coding!
